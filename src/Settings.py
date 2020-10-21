# standard
import os
import json


class SettingsAPI(object):
    """Settings API"""
    _settings_file_name = 'settings.json'
    _default_settings = {
        'white_time': 600,
        'white_style': {
            'color': 'black',
            'font-size': '200px',
            'background-color': 'white'
        },
        'black_time': 600,
        'black_style': {
            'color': 'white',
            'font-size': '200px',
            'background-color': 'black'
        }
    }

    def __init__(self):
        self._settings = None
        self._settings_path = None
        self._initialize()

    def _initialize(self):
        if os.path.exists(self.settings_path):
            with open(self.settings_path, 'rt') as f:
                self._settings = json.loads(f.read())
        else:
            self._settings = self._default_settings
            with open(self.settings_path, 'wt') as f:
                f.write(json.dumps(self._settings))

    @property
    def settings_path(self):
        if self._settings_path is None:
            self._settings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), self._settings_file_name)
        return self._settings_path

    def get(self, k, d=None):
        return self._settings.get(k, d)

    def set(self, k, v):
        self._settings[k] = v

    def save(self):
        pass
        # most define
