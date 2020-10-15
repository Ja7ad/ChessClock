# standard
import sys
# internal
from src.UI import ChessClockUI
from src.Model import ChessClockModel
from src.Controller import ChessClockController
# external
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ui = ChessClockUI()
    ui.showMaximized()
    model = ChessClockModel()
    ChessClockController(ui, model)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
