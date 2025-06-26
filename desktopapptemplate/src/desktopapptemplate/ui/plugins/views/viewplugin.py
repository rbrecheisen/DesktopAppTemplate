from desktopapptemplate.ui.plugins.plugin import Plugin


class ViewPlugin(Plugin):
    def __init__(self, name, display_name, plugin):
        super(ViewPlugin, self).__init__(name, display_name)
        self._plugin = plugin

    def plugin(self):
        return self._plugin