import os

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QIcon,
)
from PySide6.QtCore import Qt, QByteArray

import desktopapptemplate.ui.constants as constants

from desktopapptemplate.ui.settings import Settings
from desktopapptemplate.ui.panels.mainpanel import MainPanel
from desktopapptemplate.ui.utils import resource_path, version, is_macos
from desktopapptemplate.core.plugins.plugin import Plugin
from desktopapptemplate.core.plugins.pluginmanager import PluginManager
from desktopapptemplate.ui.plugins.views.viewpluginmanager import ViewPluginManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = None
        self._main_panel = None
        self._view = None
        self.init_window()

    def init_window(self):
        self.setWindowTitle(f'{constants.DESKTOPAPPTEMPLATE_WINDOW_TITLE} {version()}')
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.DESKTOPAPPTEMPLATE_RESOURCES_IMAGES_ICONS_DIR, constants.DESKTOPAPPTEMPLATE_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()
        self.init_menus()
        self.init_status_bar()
        self.setCentralWidget(self.main_panel())

    def init_menus(self):
        self.init_app_menu()
        self.init_data_menu()
        if is_macos():            
            self.menuBar().setNativeMenuBar(False)

    def init_app_menu(self):
        app_menu_open_settings_action = QAction(constants.DESKTOPAPPTEMPLATE_APP_MENU_ITEM_SETTINGS, self)
        app_menu_open_settings_action.triggered.connect(self.handle_open_settings)
        app_menu_exit_action = QAction(constants.DESKTOPAPPTEMPLATE_APP_MENU_ITEM_EXIT, self)
        app_menu_exit_action.triggered.connect(self.close)
        app_menu = self.menuBar().addMenu(constants.DESKTOPAPPTEMPLATE_APP_MENU)
        app_menu.addAction(app_menu_open_settings_action)
        app_menu.addAction(app_menu_exit_action)

    def init_data_menu(self):
        data_menu = self.menuBar().addMenu('Data')        
        manager = PluginManager()
        for plugin in manager.plugins(plugin_type=Plugin.Type.LOADER):
            data_menu_action = QAction(plugin.display_name(), self)
            self._view = ViewPluginManager.view_for(plugin)
            data_menu_action.triggered.connect(self.handle_loader_plugin_show)
            data_menu.addAction(data_menu_action)

    def init_status_bar(self):
        self.set_status(constants.DESKTOPAPPTEMPLATE_STATUS_READY)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def main_panel(self):
        if not self._main_panel:
            self._main_panel = MainPanel(self)
        return self._main_panel

    # SETTERS

    def set_status(self, message):
        self.statusBar().showMessage(message)

    # EVENT HANDLERS

    def handle_open_settings(self):
        pass

    def handle_loader_plugin_show(self):
        self._view.show()

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)
    
    # MISCELLANEOUS

    def load_geometry_and_state(self):
        geometry = self.settings().get(constants.DESKTOPAPPTEMPLATE_WINDOW_GEOMETRY_KEY)
        state = self.settings().get(constants.DESKTOPAPPTEMPLATE_WINDOW_STATE_KEY)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.settings().set(
            constants.DESKTOPAPPTEMPLATE_WINDOW_GEOMETRY_KEY, self.saveGeometry())
        self.settings().set(
            constants.DESKTOPAPPTEMPLATE_WINDOW_STATE_KEY, self.saveState())

    def set_default_size_and_position(self):
        self.resize(constants.DESKTOPAPPTEMPLATE_WINDOW_W, constants.DESKTOPAPPTEMPLATE_WINDOW_H)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))