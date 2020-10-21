# internal
from src.UI import ChessClockUI
from src.Model import ChessClockModel
from src.Settings import SettingsAPI


class ChessClockController(object):
    """Chess Clock Controller"""
    def __init__(self):
        self._ui = None
        self._model = None
        self._settings = None
        self._initialize()
        self._bootstrap()

    def _initialize(self):
        self._settings = SettingsAPI()
        self._initialize_ui()
        self._initialize_model()

    def _initialize_ui(self):
        self._ui = ChessClockUI()
        self._ui.set_style(self._settings.get('white_style'), self._settings.get('black_style'))

    def _initialize_model(self):
        self._model = ChessClockModel(self._settings.get('white_time'), self._settings.get('black_time'))

    def _bootstrap(self):
        self._connect_signals()
        self._ready()

    def _connect_signals(self):
        # ui signals
        self._ui.signals.move.connect(self._model.move)
        self._ui.signals.reset.connect(self._restart)
        # model signals
        self._model.signals.change.connect(self._ui.update_clocks)

    def _ready(self):
        self._ui.update_clocks(*self._model.get_players_time())

    def _restart(self):
        # must complete
        self._model.restart()
        self._ready()

    def show(self):
        self._ui.show()

    def show_maximize(self):
        self._ui.showMaximized()
