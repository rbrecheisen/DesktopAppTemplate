from desktopapptemplate.core.plugins.processors.processorplugin import ProcessorPlugin


class CsvProcessorPlugin(ProcessorPlugin):
    def __init__(self):
        super(CsvProcessorPlugin, self).__init__('csvprocessorplugin', 'Process CSV')