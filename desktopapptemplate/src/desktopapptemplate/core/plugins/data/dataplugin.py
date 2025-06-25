from desktopapptemplate.core.plugins.plugin import Plugin


class DataPlugin(Plugin):
    def __init__(self, name, display_name, version):
        super(DataPlugin, self).__init__(name, display_name, Plugin.Type.DATA, version)