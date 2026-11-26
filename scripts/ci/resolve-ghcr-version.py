#!/usr/bin/env python3
"""Resolve the next semver Docker tag (vX.Y.Z) for a GHCR package."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Iterable, Optional, Tuple

SEMVER_RE = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


def parse_semver(tag: str) -> Optional[Tuple[int, int, int]]:
    match = SEMVER_RE.match(tag.strip())
    if not match:
        return None
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def format_semver(version: Tuple[int, int, int]) -> str:
    return f"v{version[0]}.{version[1]}.{version[2]}"


def bump_semver(version: Tuple[int, int, int], bump: str) -> Tuple[int, int, int]:
    major, minor, patch = version
    if bump == "major":
        return (major + 1, 0, 0)
    if bump == "minor":
        return (major, minor + 1, 0)
    if bump == "patch":
        return (major, minor, patch + 1)
    raise ValueError(f"Unsupported bump type: {bump}")


def resolve_next_version(
    existing_tags: Iterable[str],
    *,
    start_version: str = "0.1.0",
    override_version: str = "",
    bump: str = "patch",
) -> Tuple[str, str]:
    """Return (vX.Y.Z, X.Y.Z) based on existing GHCR tags or explicit override."""
    if override_version.strip():
        parsed = parse_semver(override_version.strip())
        if parsed is None:
            raise ValueError(f"Invalid override version: {override_version!r}")
        tag = format_semver(parsed)
        return tag, tag.lstrip("v")

    parsed_start = parse_semver(start_version)
    if parsed_start is None:
        raise ValueError(f"Invalid start version: {start_version!r}")

    highest: Optional[Tuple[int, int, int]] = None
    for raw_tag in existing_tags:
        parsed = parse_semver(raw_tag)
        if parsed is None:
            continue
        if highest is None or parsed > highest:
            highest = parsed

    if highest is None:
        next_ver = parsed_start
    else:
        next_ver = bump_semver(highest, bump)

    tag = format_semver(next_ver)
    return tag, tag.lstrip("v")


def fetch_ghcr_tags(owner: str, package: str, token: str) -> list[str]:
    """Fetch container tags from GitHub Packages API for an org or user."""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "sensio-hub-ci",
    }
    endpoints = [
        f"https://api.github.com/orgs/{owner}/packages/container/{package}/versions?per_page=100",
        f"https://api.github.com/users/{owner}/packages/container/{package}/versions?per_page=100",
    ]
    last_error: Optional[Exception] = None
    for url in endpoints:
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
                tags: list[str] = []
                for item in payload:
                    container = (item.get("metadata") or {}).get("container") or {}
                    for t in container.get("tags") or []:
                        if isinstance(t, str):
                            tags.append(t)
                return tags
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                last_error = exc
                continue
            raise
    if isinstance(last_error, urllib.error.HTTPError) and last_error.code == 404:
        return []
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", required=True, help="GitHub org or user owner")
    parser.add_argument("--package", required=True, help="GHCR package name")
    parser.add_argument("--start-version", default="0.1.0")
    parser.add_argument("--override-version", default="")
    parser.add_argument("--bump", default="patch", choices=("patch", "minor", "major"))
    parser.add_argument("--github-output", default=os.environ.get("GITHUB_OUTPUT", ""))
    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    existing_tags: list[str] = []
    if not args.override_version.strip() and token:
        existing_tags = fetch_ghcr_tags(args.owner, args.package, token)

    tag, bare = resolve_next_version(
        existing_tags,
        start_version=args.start_version,
        override_version=args.override_version,
        bump=args.bump,
    )

    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"version={tag}\n")
            fh.write(f"bare_version={bare}\n")

    print(f"version={tag}")
    print(f"bare_version={bare}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
