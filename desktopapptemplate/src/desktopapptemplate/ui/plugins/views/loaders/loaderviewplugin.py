from PySide6.QtWidgets import QDialog

from desktopapptemplate.ui.plugins.views.viewplugin import ViewPlugin


class LoaderViewPLugin(ViewPlugin, QDialog):
    def __init__(self, name, display_name, version):
        super(LoaderViewPLugin, self).__init__(name, display_name, version)