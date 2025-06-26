from PySide6.QtWidgets import (
    QTextEdit,
    QFileDialog,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from desktopapptemplate.ui.components.dialog import Dialog


class CsvLoaderDialog(Dialog):
    def __init__(self, parent=None):
        super(CsvLoaderDialog, self).__init__(parent)
        self._file_path_text_edit = None
        self._open_file_dialog_button = None
        self._close_button = None
        self._file_path = None
        self.init_layout()

    def file_path_text_edit(self):
        if not self._file_path_text_edit:
            self._file_path_text_edit = QTextEdit(placeholderText='Enter file path')
        return self._file_path_text_edit
    
    def open_file_dialog_button(self):
        if not self._open_file_dialog_button:
            self._open_file_dialog_button = QPushButton('Select file path')
            self._open_file_dialog_button.clicked.connect(self.handle_open_file_dialog)
        return self._open_file_dialog_button
    
    def close_button(self):
        if not self._close_button:
            self._close_button = QPushButton('Close')
            self._close_button.clicked.connect(self.accept)
        return self._close_button
    
    def file_path(self):
        return self._file_path

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_text_edit())
        layout.addWidget(self.open_file_dialog_button())
        layout.addWidget(self.close_button())
        self.setLayout(layout)

    def handle_open_file_dialog(self):
        self._file_path, _ = QFileDialog.getOpenFileName(self)
        if self._file_path:
            self.file_path_text_edit().setText(self._file_path)