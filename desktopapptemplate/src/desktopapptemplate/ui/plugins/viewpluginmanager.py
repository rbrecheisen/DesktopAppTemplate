from desktopapptemplate.ui.plugins.loaders.csvloaderviewplugin import CsvLoaderViewPlugin
from desktopapptemplate.core.plugins.loaders.loaderpluginmanager import LoaderPluginManager
from desktopapptemplate.core.singleton import singleton


@singleton
class ViewPluginManager:
    def __init__(self):
        self._plugins = {}
        self.load_plugins()

    def load_plugins(self):
        manager = LoaderPluginManager()
        csvloaderplugin = manager.plugin('csvloaderplugin')
        csvloaderviewplugin = CsvLoaderViewPlugin(csvloaderplugin)
        self._plugins = {
            csvloaderviewplugin.name(): csvloaderviewplugin,
        }

    def plugins(self):
        return self._plugins.items()
    
    def plugin(self, name):
        if name in self._plugins.keys():
            return self._plugins[name]
        raise RuntimeError(f'Plugin "{name}" not found')
    
    def view_for(self, plugin):
        for _, view_plugin in self.plugins():
            if plugin.name() == view_plugin.plugin().name():
                return view_plugin
        raise RuntimeError(f'Could not find view plugin for plugin "{plugin.name()}"')