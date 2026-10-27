from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.shell import Shell
from src.config import Config
from src.startup import load_script

class TerminalWindow(QMainWindow):
    """Графическая оболочка эмулятора."""

    def __init__(self, config: Config):
        super().__init__()

        self.config = config
        self.shell = Shell()

        self.setWindowTitle("Shell Emulator (VFS)")
        self.resize(800, 500)

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)

        self.command_input = QLineEdit()
        self.command_input.setPlaceholderText("Enter command...")

        self.command_input.returnPressed.connect(
            self.run_command
        )

        layout = QVBoxLayout()
        layout.addWidget(self.output)
        layout.addWidget(self.command_input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            QPlainTextEdit, QLineEdit {
                background-color: #161b22;
                color: #c9d1d9;
                font-family: monospace;
                font-size: 14px;
                border: 1px solid #30363d;
                padding: 8px;
            }
        """)

        self.output.appendPlainText("")
        self.command_input.setFocus()

    def execute_command(self, line: str) -> bool:
        """Выполнить команду и вывести результат."""
        if not line.strip():
            return False

        self.output.appendPlainText(f"> {line}")

        result, should_exit = self.shell.execute(line)

        if result:
            self.output.appendPlainText(result)

        if should_exit:
            self.close()

        return should_exit

    def run_command(self):
        """Обработать команду пользователя."""
        line = self.command_input.text()
        self.command_input.clear()

        self.execute_command(line)

    def run_script(self):
        """Выполнить стартовый скрипт."""
        if self.config.script_path is None:
            return

        try:
            commands = load_script(self.config.script_path)
        except (OSError, UnicodeError) as error:
            self.output.appendPlainText(
                f"Script error: {error}"
            )
            return

        for command in commands:
            should_exit = self.execute_command(command)

            if should_exit:
                break
