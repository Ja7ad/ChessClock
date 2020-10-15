# standard
from time import sleep
from threading import Thread
# external
from PyQt5.QtCore import QObject, pyqtSignal


class ChessPlayer(object):
    """Chess Player"""
    def __init__(self, _time):
        self._time = _time

    def get_time(self):
        return self._time

    def inc_time(self):
        self._time += 1

    def dec_time(self):
        if self._time - 1 < 0:
            self._time = 0
        else:
            self._time -= 1


class ChessClockModelSignals(QObject):
    """Chess Clock Model Signals"""
    result = pyqtSignal(int, int)


class ChessClockModel(object):
    """Chess Clock Model"""
    def __init__(self):
        self._settings = {
            'white_time': 120,
            'black_time': 120
        }
        self._white = ChessPlayer(self._settings['white_time'])
        self._black = ChessPlayer(self._settings['black_time'])
        self._turns = {1: self._white, -1: self._black}
        self._turn = 1
        self._thread = None
        self._running = False
        self.signals = ChessClockModelSignals()

    def _game_is_on(self):
        return self._white.get_time() and self._black.get_time()

    def _waiting(self):
        while self._running:
            c = 0
            while self._running and c < 10:
                sleep(0.1)
                c += 1
            if c == 10:
                self._turns[self._turn].dec_time()
            self.signals.result.emit(self._white.get_time(), self._black.get_time())

    def move(self):
        if not self._game_is_on():
            return
        if self._thread is not None and self._thread.is_alive():
            self._running = False
            self._thread.join()
        self._turn *= -1
        self._thread = Thread(target=self._waiting)
        self._running = True
        self._thread.start()

    def reset(self):
        pass
