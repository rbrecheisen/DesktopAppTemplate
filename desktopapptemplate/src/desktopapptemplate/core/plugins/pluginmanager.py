from desktopapptemplate.core.plugins.plugin import Plugin
from desktopapptemplate.core.plugins.data.csvdataplugin import CsvDataPlugin
from desktopapptemplate.core.plugins.loaders.csvloaderplugin import CsvLoaderPlugin
from desktopapptemplate.core.plugins.processors.csvprocessorplugin import CsvProcessorPlugin


class PluginManager:
    def __init__(self):
        self._plugins = {}

    def load_plugins(self):
        return {
            'csvdataplugin': CsvDataPlugin('csvdataplugin', 'CSV', '1.0'),
            'csvloaderplugin': CsvLoaderPlugin('csvloaderplugin', 'Load CSV data...', '1.0'),
            'csvprocessorplugin': CsvProcessorPlugin('csvprocessorplugin', 'Process CSV...', '1.0'),
        }

    def plugins(self, plugin_type=None):
        if len(self._plugins.keys()) == 0:
            self._plugins = self.load_plugins()
        if plugin_type:
            plugins = []
            assert isinstance(plugin_type, Plugin.Type)
            for plugin in self._plugins.values():
                if plugin.type() == plugin_type:
                    plugins.append(plugin)
            return plugins
        return self._plugins.values()