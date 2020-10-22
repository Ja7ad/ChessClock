# external
from PyQt5.QtCore import QObject, QTimer, pyqtSignal


class ChessPlayer(object):
    """Chess Player"""
    def __init__(self, _time):
        self._time = _time
        self._dec = 0
        self._inc = 0

    def get_time(self):
        return self._time + self._inc - self._dec

    def inc_time(self):
        self._inc += 1

    def dec_time(self):
        if self.get_time() - 1 >= 0:
            self._dec += 1

    def reset_time(self):
        self._dec = 0
        self._inc = 0


class ChessClockModelSignals(QObject):
    """Chess Clock Model Signals"""
    change = pyqtSignal(int, int)


class ChessClockModel(object):
    """Chess Clock Model"""
    def __init__(self, white_time, black_time):
        self._players = {1: ChessPlayer(white_time), -1: ChessPlayer(black_time)}
        self._turn = 1
        self._timer = QTimer()
        self._timer.timeout.connect(self._waiting)
        self.signals = ChessClockModelSignals()

    def get_players_time(self):
        return self._players[1].get_time(), self._players[-1].get_time()

    def _game_is_on(self):
        w, b = self.get_players_time()
        return w and b

    def _stop_timer(self):
        if self._timer.isActive():
            self._timer.stop()

    def _waiting(self):
        self._players[self._turn].dec_time()
        self.signals.change.emit(*self.get_players_time())

    def move(self):
        self._stop_timer()
        if not self._game_is_on():
            return
        self._turn *= -1
        self._timer.start(1000)

    def restart(self):
        self._stop_timer()
        self._turn = 1
        for player in self._players.values():
            player.reset_time()
