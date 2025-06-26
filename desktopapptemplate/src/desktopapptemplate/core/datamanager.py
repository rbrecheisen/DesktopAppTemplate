from desktopapptemplate.core.singleton import singleton


@singleton()
class DataManager:
    def __init__(self):
        self._data_plugins = {}

    def add_data_plugin(self, data_plugin):
        pass