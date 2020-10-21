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
        for name in ['white_clock', 'black_clock']:
            wrapper = QVBoxLayout()
            c = QLabel()
            c.setAlignment(Qt.AlignCenter)
            setattr(self, name, c)
            wrapper.addWidget(getattr(self, name))
            self.general_layout.addLayout(wrapper)

    @staticmethod
    def _clock_format(_time):
        mins, secs = divmod(_time, 60)
        return '{:02d}:{:02d}'.format(mins, secs)

    def set_style(self, white_style, black_style):
        s = 'color:{color};font-size:{font-size};background-color:{background-color};'
        self.white_clock.setStyleSheet(s.format(**white_style))
        self.black_clock.setStyleSheet(s.format(**black_style))

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
