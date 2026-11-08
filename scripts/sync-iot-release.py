#!/usr/bin/env python3
"""Sync Sensio IoT release info into sensio-hub docs and manifests."""
import os
import re
from pathlib import Path


def main():
    version = os.environ["VERSION"]
    tag = os.environ["TAG"]
    apk = os.environ["APK_NAME"]
    sha256 = os.environ["SHA256"]

    doc_path = Path("docs/iot/install-android.md")
    content = doc_path.read_text(encoding="utf-8")

    section = (
        "## 1. Downloading the APK\n\n"
        "Pre-signed APK packages are published on GitHub Releases:\n\n"
        "- **Latest Stable Release**: [Sensio IoT Releases](https://github.com/BIG-FullFill/sensio-hub/releases)\n"
        f"- **Direct Download (v{version})**: [{apk}](https://github.com/BIG-FullFill/sensio-hub/releases/download/{tag}/{apk})\n"
        "- **Verified SHA-256 Checksum**:\n"
        f"  ```\n  {sha256}\n  ```\n\n"
        "---\n\n"
    )

    updated = re.sub(
        r"## 1\. Downloading the APK.*?(?=## 2\.)",
        section,
        content,
        flags=re.DOTALL,
    )
    doc_path.write_text(updated, encoding="utf-8")
    print(f"Updated docs/iot/install-android.md for {tag} ({apk})")


if __name__ == "__main__":
    main()
