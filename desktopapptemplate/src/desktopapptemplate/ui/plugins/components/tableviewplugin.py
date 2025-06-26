from desktopapptemplate.core.plugins.plugin import Plugin
from desktopapptemplate.ui.plugins.viewplugin import ViewPlugin


class TableViewPlugin(ViewPlugin):
    def __init__(self, display_name, plugin):
        super(TableViewPlugin, self).__init__('tableviewplugin', display_name, plugin)
        if not isinstance(self.plugin(), Plugin.Type.DATA):
            raise RuntimeError(f'Plugin "{plugin.name()}" is not a data plugin')