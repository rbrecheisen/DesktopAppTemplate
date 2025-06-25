from PySide6.QtWidgets import QWidget

from desktopapptemplate.core.plugins.plugin import Plugin


class Plugin(QWidget, Plugin):
    def __init__(self, name, display_name, version):
        super(Plugin, self).__init__()
        self._name = name
        self._display_name = display_name
        self._version = version

    def name(self):
        return self._name
    
    def display_name(self):
        return self._display_name
    
    def version(self):
        return self._version