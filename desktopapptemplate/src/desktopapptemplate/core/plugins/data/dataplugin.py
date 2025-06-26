from desktopapptemplate.core.plugins.plugin import Plugin


class DataPlugin(Plugin):
    def __init__(self, name, display_name):
        super(DataPlugin, self).__init__(name, display_name, Plugin.Type.DATA)
        self._data = None

    def data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data