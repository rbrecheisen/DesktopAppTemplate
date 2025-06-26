from PySide6.QtWidgets import QWidget


class Plugin(QWidget):
    def __init__(self, name, display_name):
        super(Plugin, self).__init__()
        self._name = name
        self._display_name = display_name

    def name(self):
        return self._name
    
    def display_name(self):
        return self._display_name