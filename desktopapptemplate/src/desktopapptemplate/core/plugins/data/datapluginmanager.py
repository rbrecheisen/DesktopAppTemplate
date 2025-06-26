from desktopapptemplate.core.plugins.pluginmanager import PluginManager
from desktopapptemplate.core.plugins.data.csvdataplugin import CsvDataPlugin


class DataPluginManager(PluginManager):
    def __init__(self):
        super(DataPluginManager, self).__init__()

    def load_plugins(self):
        csvdataplugin = CsvDataPlugin()
        return {
            csvdataplugin.name(): csvdataplugin,
        }