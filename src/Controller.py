class ChessClockController(object):
    """Chess Clock Controller"""
    def __init__(self, ui, model):
        self._ui = ui
        self._model = model
        self._bootstrap()

    def _bootstrap(self):
        self._connect_signals()

    def _connect_signals(self):
        # ui signals
        self._ui.signals.move.connect(self._model.move)
        self._ui.signals.reset.connect(self._model.reset)
        # model signals
        self._model.signals.result.connect(self._ui.update_clocks)
