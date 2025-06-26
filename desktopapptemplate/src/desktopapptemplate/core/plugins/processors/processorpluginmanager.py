from desktopapptemplate.core.plugins.pluginmanager import PluginManager
from desktopapptemplate.core.plugins.processors.csvprocessorplugin import CsvProcessorPlugin


class ProcessorPluginManager(PluginManager):
    def __init__(self):
        super(ProcessorPluginManager, self).__init__()

    def load_plugins(self):
        csvprocessorplugin = CsvProcessorPlugin()
        return {
            csvprocessorplugin.name(): csvprocessorplugin,
        }