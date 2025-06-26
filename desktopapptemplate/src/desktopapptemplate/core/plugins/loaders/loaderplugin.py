from desktopapptemplate.core.plugins.plugin import Plugin


class LoaderPlugin(Plugin):
    def __init__(self, name, display_name):
        super(LoaderPlugin, self).__init__(name, display_name, Plugin.Type.LOADER)