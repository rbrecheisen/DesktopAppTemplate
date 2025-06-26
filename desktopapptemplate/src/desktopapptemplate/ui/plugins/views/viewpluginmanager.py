from desktopapptemplate.ui.plugins.pluginmanager import PluginManager


class ViewPluginManager(PluginManager):
    def __init__(self):
        super(ViewPluginManager, self).__init__()

    def load_plugins(self):
        pass

    def view(self, name):
        return self.plugin(name)

    def view_for(self, plugin):
        return None