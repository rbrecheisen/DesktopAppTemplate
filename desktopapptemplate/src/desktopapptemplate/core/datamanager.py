from desktopapptemplate.core.singleton import singleton


@singleton()
class DataManager:
    def __init__(self):
        self._data = {}

    # Add objects with a DataPlugin interface
    def add_data(self, data):
        pass