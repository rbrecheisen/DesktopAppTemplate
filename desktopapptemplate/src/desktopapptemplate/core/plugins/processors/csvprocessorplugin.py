from desktopapptemplate.core.plugins.processors.processorplugin import ProcessorPlugin


class CsvProcessorPlugin(ProcessorPlugin):
    def __init__(self, name, display_name, version):
        super(CsvProcessorPlugin, self).__init__(name, display_name, version)