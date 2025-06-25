from desktopapptemplate.core.plugins.plugin import Plugin


class LoaderPlugin(Plugin):
    def __init__(self, name, version):
        super(LoaderPlugin, self).__init__(name, version)