from PySide6.QtWidgets import QWidget


class ViewPlugin(QWidget):
    def __init__(self, name, display_name, plugin):
        super(ViewPlugin, self).__init__()
        self._name = name
        self._display_name = display_name
        self._plugin = plugin

    def name(self):
        return self._name
    
    def display_name(self):
        return self._display_name
    
    def plugin(self):
        return self._plugin