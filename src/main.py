import sys

from PyQt6.QtWidgets import QApplication
from src.gui import TerminalWindow

def main() -> int:
    """ главная функция """
    app = QApplication(sys.argv)

    window = TerminalWindow()
    window.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
