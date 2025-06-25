from desktopapptemplate.core.plugins.plugin import Plugin


class ProcessorPlugin(Plugin):
    def __init__(self, name, version):
        super(ProcessorPlugin, self).__init__(name, version)