from PySide6.QtWidgets import QDialog

from desktopapptemplate.ui.plugins.viewplugin import ViewPlugin


class LoaderViewPlugin(ViewPlugin):
    def __init__(self, name, display_name, plugin):
        super(LoaderViewPlugin, self).__init__(name, display_name, plugin)