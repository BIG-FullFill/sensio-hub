import importlib.util
from pathlib import Path
import unittest


def load_module():
    path = Path(__file__).with_name("resolve-ghcr-version.py")
    spec = importlib.util.spec_from_file_location("resolve_ghcr_version", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


mod = load_module()


class ResolveGhcrVersionTests(unittest.TestCase):
    def test_starts_at_v0_1_0_when_no_tags_exist(self):
        self.assertEqual(mod.resolve_next_version([]), ("v0.1.0", "0.1.0"))
        self.assertEqual(mod.resolve_next_version(["latest", "sha-abc123"]), ("v0.1.0", "0.1.0"))

    def test_bumps_highest_semver_patch(self):
        tags = ["latest", "v0.1.0", "v0.1.2", "v0.1.1"]
        self.assertEqual(mod.resolve_next_version(tags), ("v0.1.3", "0.1.3"))

    def test_bumps_minor_and_major(self):
        tags = ["v0.1.9"]
        self.assertEqual(mod.resolve_next_version(tags, bump="minor"), ("v0.2.0", "0.2.0"))
        self.assertEqual(mod.resolve_next_version(tags, bump="major"), ("v1.0.0", "1.0.0"))

    def test_override_version_wins(self):
        self.assertEqual(
            mod.resolve_next_version(["v0.1.4"], override_version="0.5.0"),
            ("v0.5.0", "0.5.0"),
        )
        self.assertEqual(
            mod.resolve_next_version(["v0.1.4"], override_version="v1.2.3"),
            ("v1.2.3", "1.2.3"),
        )

    def test_invalid_override_raises(self):
        with self.assertRaises(ValueError):
            mod.resolve_next_version([], override_version="bad-tag")


if __name__ == "__main__":
    unittest.main()
