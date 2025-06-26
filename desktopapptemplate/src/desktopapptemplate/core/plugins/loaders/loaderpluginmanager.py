from desktopapptemplate.core.plugins.pluginmanager import PluginManager
from desktopapptemplate.core.plugins.loaders.csvloaderplugin import CsvLoaderPlugin


class LoaderPluginManager(PluginManager):
    def __init__(self):
        super(LoaderPluginManager, self).__init__()

    def load_plugins(self):
        csvloaderplugin = CsvLoaderPlugin()
        return {
            csvloaderplugin.name(): csvloaderplugin,
        }