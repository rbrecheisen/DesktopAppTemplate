from desktopapptemplate.core.plugins.processors.processorplugin import ProcessorPlugin


class CsvProcessorPlugin(ProcessorPlugin):
    def __init__(self, name, version):
        super(CsvProcessorPlugin, self).__init__(name, version)