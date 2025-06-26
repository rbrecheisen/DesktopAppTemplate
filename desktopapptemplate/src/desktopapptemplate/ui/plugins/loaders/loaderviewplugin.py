from PySide6.QtWidgets import QDialog

from desktopapptemplate.ui.plugins.plugin import Plugin


class LoaderViewPLugin(Plugin):
    def __init__(self, name, display_name, plugin):
        super(LoaderViewPLugin, self).__init__(name, display_name, plugin)
        self._dialog = QDialog()
        self._dialog.setWindowTitle(display_name)

    def show(self):
        self._dialog.exec()