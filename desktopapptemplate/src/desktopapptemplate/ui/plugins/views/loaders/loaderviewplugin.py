from PySide6.QtWidgets import QDialog

from desktopapptemplate.ui.plugins.views.viewplugin import ViewPlugin


class LoaderViewPLugin(ViewPlugin):
    def __init__(self, name, display_name, version):
        super(LoaderViewPLugin, self).__init__(name, display_name, version)
        self._dialog = QDialog()
        self._dialog.setWindowTitle('LoaderViewPlugin')

    def show(self):
        print('showing loader view dialog...')
        self._dialog.exec_()