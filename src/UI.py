# external
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel


class ChessClockUISignals(QObject):
    """Chess Clock UI Signals"""
    move = pyqtSignal()
    reset = pyqtSignal()


class ChessClockUI(QMainWindow):
    """Chess Clock UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Chess Clock')
        self.general_layout = QHBoxLayout()
        self._centeral_widget = QWidget(self)
        self._centeral_widget.setLayout(self.general_layout)
        self.setCentralWidget(self._centeral_widget)

        # signals
        self.signals = ChessClockUISignals()
        # create ui
        self._create_ui()

    def _create_ui(self):
        clocks = [
            {
                'name': 'white_clock',
                'style': {'clr': 'black', 'bg-clr': 'white', 'fs': '200px'}
            },
            {
                'name': 'black_clock',
                'style': {'clr': 'white', 'bg-clr': 'black', 'fs': '200px'}
            }
        ]
        for clock in clocks:
            wrapper = QVBoxLayout()
            c = QLabel()
            c.setAlignment(Qt.AlignCenter)
            c.setStyleSheet('color: {clr}; background-color: {bg-clr}; font-size: {fs}'.format(**clock['style']))
            setattr(self, clock['name'], c)
            wrapper.addWidget(getattr(self, clock['name']))
            self.general_layout.addLayout(wrapper)

    @staticmethod
    def _clock_format(_time):
        mins, secs = divmod(_time, 60)
        return '{:02d}:{:02d}'.format(mins, secs)

    def update_clocks(self, white_time, black_time):
        self.white_clock.setText(self._clock_format(white_time))
        self.black_clock.setText(self._clock_format(black_time))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.signals.move.emit()
        elif event.key() == Qt.Key_R:
            self.signals.reset.emit()
        elif event.key() == Qt.Key_Escape:
            self.close()
