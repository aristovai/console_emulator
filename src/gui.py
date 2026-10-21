from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.shell import Shell

class TerminalWindow(QMainWindow):
    """Графическая оболочка эмулятора"""

    def __init__(self):
        super().__init__()

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

        self.command_input.setFocus()

    def run_command(self):
        """обработать введённую команду"""
        line = self.command_input.text()
        self.command_input.clear()

        if not line.strip():
            return

        self.output.appendPlainText(f"> {line}")

        result, should_exit = self.shell.execute(line)

        if result:
            self.output.appendPlainText(result)

        if should_exit:
            self.close()