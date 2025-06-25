from PySide6.QtWidgets import QStyle

from desktopapptemplate.ui.utils import is_macos


DESKTOPAPPTEMPLATE_WINDOW_TITLE = 'DesktopAppTemplate'
DESKTOPAPPTEMPLATE_NAME = 'DesktopAppTemplate'
DESKTOPAPPTEMPLATE_BUNDLE_IDENTIFIER = 'com.rbeesoft'
DESKTOPAPPTEMPLATE_WINDOW_W = 1024
DESKTOPAPPTEMPLATE_WINDOW_H = 600
DESKTOPAPPTEMPLATE_WINDOW_GEOMETRY_KEY = 'window/geometry'
DESKTOPAPPTEMPLATE_WINDOW_STATE_KEY = 'window/state'
DESKTOPAPPTEMPLATE_STATUS_READY = 'Ready'
DESKTOPAPPTEMPLATE_DONATE_URL = 'https://rbeesoft.nl/wordpress/'

DESKTOPAPPTEMPLATE_RESOURCES_DIR = 'desktopapptemplate/resources'
DESKTOPAPPTEMPLATE_RESOURCES_IMAGES_DIR = 'desktopapptemplate/resources/images'
DESKTOPAPPTEMPLATE_RESOURCES_IMAGES_ICONS_DIR = 'desktopapptemplate/resources/images/icons'
DESKTOPAPPTEMPLATE_RESOURCES_ICON = 'desktopapptemplate.icns' if is_macos() else 'desktopapptemplate.ico'

DESKTOPAPPTEMPLATE_LAST_DIRECTORY_KEY = 'desktopapptemplate/last_directory'

# https://www.pythonguis.com/faq/built-in-qicons-pyqt/#qt-standard-icons
DESKTOPAPPTEMPLATE_ICON_EXIT = QStyle.SP_MessageBoxCritical
DESKTOPAPPTEMPLATE_ICON_SETTINGS = QStyle.SP_VistaShield