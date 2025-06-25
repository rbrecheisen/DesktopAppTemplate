import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)

import desktopapptemplate.ui.constants as constants

from desktopapptemplate.ui.settings import Settings
from desktopapptemplate.ui.panels.logpanel import LogPanel
from desktopapptemplate.core.logging import LogManager

LOG = LogManager()


class MainPanel(QWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._donate_button = None
        self._input_directory_button = None
        self._input_directory = None
        self._output_directory_button = None
        self._output_directory = None
        self._run_pipeline_button = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        layout = QVBoxLayout()
        layout.addWidget(self.donate_button())
        layout.addWidget(self.input_directory_button())
        layout.addWidget(self.output_directory_button())
        layout.addWidget(self.run_pipeline_button())
        layout.addWidget(self.log_panel())
        self.setLayout(layout)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton('Please donate!')
            self._donate_button.setStyleSheet('background-color: blue; color: white; font-weight: bold;')
            self._donate_button.clicked.connect(self.handle_donate)
        return self._donate_button

    def input_directory_button(self):
        if not self._input_directory_button:
            self._input_directory_button = QPushButton('Select input directory')
            self._input_directory_button.clicked.connect(self.handle_open_input_directory)
        return self._input_directory_button
    
    def input_directory(self):
        return self._input_directory
    
    def set_input_directory(self, directory):
        self._input_directory = directory
        self.output_directory_button().setEnabled(True)
    
    def output_directory_button(self):
        if not self._output_directory_button:
            self._output_directory_button = QPushButton('Select output directory')
            self._output_directory_button.clicked.connect(self.handle_open_output_directory)
            self._output_directory_button.setEnabled(False)
        return self._output_directory_button
    
    def output_directory(self):
        return self._output_directory
    
    def set_output_directory(self, directory):
        self._output_directory = directory
        self.run_pipeline_button().setEnabled(True)

    def run_pipeline_button(self):
        if not self._run_pipeline_button:
            self._run_pipeline_button = QPushButton('Run pipeline')
            self._run_pipeline_button.clicked.connect(self.handle_run_pipeline)
            self._run_pipeline_button.setEnabled(False)
        return self._run_pipeline_button
    
    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel

    # EVENT HANDLERS

    def handle_donate(self):
        webbrowser.open(constants.DESKTOPAPPTEMPLATE_DONATE_URL)

    def handle_open_input_directory(self):
        last_directory = self.settings().get(constants.DESKTOPAPPTEMPLATE_LAST_DIRECTORY_KEY)
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.set_input_directory(directory)
            self.settings().set(constants.DESKTOPAPPTEMPLATE_LAST_DIRECTORY_KEY, directory)

    def handle_open_output_directory(self):
        last_directory = self.settings().get(constants.DESKTOPAPPTEMPLATE_LAST_DIRECTORY_KEY)
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.set_output_directory(directory)

    def handle_run_pipeline(self):
        pass