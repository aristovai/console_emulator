import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from src.gui import TerminalWindow
from src.config import parse_arguments

def main() -> int:
    """ главная функция """
    config = parse_arguments()
    print(f"vfs:    {config.vfs_path}")
    print(f"script: {config.script_path}")


    app = QApplication(sys.argv)

    window = TerminalWindow(config)
    window.show()

    if config.script_path is not None:
        QTimer.singleShot(0, window.run_script)
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
