from desktopapptemplate.core.plugins.pluginmanager import PluginManager


class ViewPluginManager:
    def __init__(self):
        self._plugin_manager = PluginManager()

    def view_for(self, plugin):
        