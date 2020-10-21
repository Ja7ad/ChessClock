# standard
from time import sleep
# external
from PyQt5.QtCore import QObject, pyqtSignal, QThread


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
    change = pyqtSignal(int, int)


class CThread(QThread):
    """Chess Thread"""
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        super().__init__()

    def run(self):
        self._func(*self._args, **self._kwargs)


class ChessClockModel(object):
    """Chess Clock Model"""
    def __init__(self, white_time, black_time):
        self._white_time = white_time
        self._black_time = black_time
        self._players = {1: ChessPlayer(self._white_time), -1: ChessPlayer(self._black_time)}
        self._turn = 1
        self._thread = None
        self.signals = ChessClockModelSignals()

    def get_players_time(self):
        return self._players[1].get_time(), self._players[-1].get_time()

    def _game_is_on(self):
        w, b = self.get_players_time()
        return w and b

    def _waiting(self):
        while self._players[self._turn].get_time() > 0:
            sleep(1)
            self._players[self._turn].dec_time()
            self.signals.change.emit(*self.get_players_time())

    def move(self):
        if self._thread is not None and self._thread.isRunning():
            self._thread.terminate()
        if not self._game_is_on():
            return
        self._turn *= -1
        self._thread = CThread(self._waiting)
        self._thread.start()

    def restart(self):
        # must define
        pass
