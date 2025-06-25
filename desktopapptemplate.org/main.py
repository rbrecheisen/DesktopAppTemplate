import sys

from PySide6 import QtWidgets

import desktopapptemplate.ui.constants as constants

from desktopapptemplate.ui.settings import Settings
from desktopapptemplate.ui.mainwindow import MainWindow


def app():
    settings = Settings()
    application_name = settings.get(constants.MOSAMATIC_DESKTOP_WINDOW_TITLE)
    # QtWidgets.QApplication.setApplicationName(application_name)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(application_name)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app()
