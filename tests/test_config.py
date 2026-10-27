import unittest
from pathlib import Path

from src.config import parse_arguments

class TestConfig(unittest.TestCase):
    def test_no_arguments(self):
        config = parse_arguments([])
        self.assertIsNone(config.vfs_path)
        self.assertIsNone(config.script_path)

    def test_vfs_argument(self):
        config = parse_arguments(["--vfs", "test.xml"])
        self.assertEqual(config.vfs_path, Path('test.xml'))

    def test_script_argument(self):
        config = parse_arguments(["--script", "test.txt"])
        self.assertEqual(config.script_path, Path('test.txt'))

    def test_all_arguments(self):
        config = parse_arguments(["--vfs", "test.xml", "--script", "test.txt"])
        self.assertEqual(config.vfs_path, Path('test.xml'))
        self.assertEqual(config.script_path, Path('test.txt'))

    def test_unknown_argument(self):
        with self.assertRaises(SystemExit):
            parse_arguments(["--cnkj"])


if __name__ == "__main__":
    unittest.main()