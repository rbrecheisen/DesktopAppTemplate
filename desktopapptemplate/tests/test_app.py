import pytest

from desktopapptemplate.ui.mainwindow import MainWindow


@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    return window


def test_load_csv_data(main_window, qtbot):
    pass