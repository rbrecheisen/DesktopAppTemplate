from desktopapptemplate.core.plugins.pluginmanager import PluginManager
from desktopapptemplate.core.plugins.loaders.csvloaderplugin import CsvLoaderPlugin
from desktopapptemplate.ui.plugins.views.loaders.csvloaderviewplugin import CsvLoaderViewPLugin


class ViewPluginManager:
    def __init__(self):
        self._plugin_manager = PluginManager()

    @staticmethod
    def view_for(plugin):
        if isinstance(plugin, CsvLoaderPlugin):
            return CsvLoaderViewPLugin('x', 'x', '1.0') # Pass plugin as argument?
        return None