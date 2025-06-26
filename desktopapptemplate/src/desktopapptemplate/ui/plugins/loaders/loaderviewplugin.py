from PySide6.QtWidgets import QDialog

from desktopapptemplate.ui.plugins.viewplugin import ViewPlugin


class LoaderViewPlugin(ViewPlugin):
    def __init__(self, name, display_name, plugin):
        super(LoaderViewPlugin, self).__init__(name, display_name, plugin)
        self._dialog = None

    def dialog(self):
        if not self._dialog:
            self._dialog = QDialog()
            self._dialog.setWindowTitle(self.display_name())
        return self._dialog

    def show(self):
        self.dialog().exec()