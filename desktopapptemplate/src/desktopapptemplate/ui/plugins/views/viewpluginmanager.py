from desktopapptemplate.ui.plugins.pluginmanager import PluginManager
from desktopapptemplate.core.plugins.loaders.loaderpluginmanager import LoaderPluginManager
from desktopapptemplate.ui.plugins.views.loaders.csvloaderviewplugin import CsvLoaderViewPLugin


class ViewPluginManager(PluginManager):
    def __init__(self):
        super(ViewPluginManager, self).__init__()
        self.load_plugins()

    def load_plugins(self):
        manager = LoaderPluginManager()
        csvloaderplugin = manager.plugin('csvloaderplugin')
        csvloaderviewplugin = CsvLoaderViewPLugin(csvloaderplugin)
        self._plugins = {
            csvloaderviewplugin.name(): csvloaderviewplugin,
        }

    def view_for(self, plugin):
        for plugin_name, view_plugin in self.plugins():
            p = view_plugin.plugin()
            if plugin.name() == p.name():
                return view_plugin
        raise RuntimeError(f'Could not find view plugin for plugin "{plugin.name()}"')