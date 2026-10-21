import unittest

from src.shell import Shell

class TestShell(unittest.TestCase):
    """Тесты интерпретатора команд."""

    def setUp(self):
        self.shell = Shell()

    def test_parse(self):
        command, args = self.shell.parse("ls -l /home")
        self.assertEqual(command, "ls")
        self.assertEqual(args, ["-l", "/home"])

    def test_empty_input(self):
        result = self.shell.execute("")
        self.assertEqual(result, ("", False))

    def test_ls(self):
        result = self.shell.execute("ls -a")
        self.assertEqual(
            result,
            ("ls: arguments = ['-a']", False)
        )

    def test_cd(self):
        result = self.shell.execute("cd /home")
        self.assertEqual(
            result,
            ("cd: arguments = ['/home']", False)
        )

    def test_unknown_command(self):
        result = self.shell.execute("pwd")
        self.assertEqual(
            result,
            ("pwd: command not found", False)
        )

    def test_exit(self):
        result = self.shell.execute("exit")
        self.assertEqual(result, ("", True))

    def test_exit_with_arguments(self):
        result = self.shell.execute("exit 123")
        self.assertEqual(
            result,
            ("exit: too many arguments", False)
        )


if __name__ == "__main__":
    unittest.main()
