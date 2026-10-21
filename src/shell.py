class Shell:
    """интерпретатор команд"""

    def parse(self, line: str) -> tuple[str, list[str]]:
        """разделить ввод на команду и аргументы"""
        parts = line.strip().split()

        if not parts:
            return "", []

        return parts[0], parts[1:]

    def execute(self, line: str) -> tuple[str, bool]:
        """выполнить команду и вернуть результат"""
        command, args = self.parse(line)

        if not command:
            return "", False

        if command == "ls":
            return f"ls: arguments = {args}", False

        if command == "cd":
            return f"cd: arguments = {args}", False

        if command == "exit":
            if args:
                return "exit: too many arguments", False
            return "", True

        return f"{command}: command not found", False