from PySide6.QtWidgets import QDialog


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

    def add_label(self, text):
        pass

    def add_text_edit(self, placeholder=None):
        pass

    def add_button(self, text, callback):
        pass

    def init_layout(self):
        pass