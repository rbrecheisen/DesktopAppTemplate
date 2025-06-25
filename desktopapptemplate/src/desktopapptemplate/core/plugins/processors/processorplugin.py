from desktopapptemplate.core.plugins.plugin import Plugin


class ProcessorPlugin(Plugin):
    def __init__(self, name, display_name, version):
        super(ProcessorPlugin, self).__init__(name, display_name, Plugin.Type.PROCESSOR, version)