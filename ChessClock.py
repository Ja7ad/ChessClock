#!.venv/bin/python
# standard
import sys
# internal
from src.Controller import ChessClockController
# external
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    chess_clock_controller = ChessClockController()
    chess_clock_controller.show_maximize()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
