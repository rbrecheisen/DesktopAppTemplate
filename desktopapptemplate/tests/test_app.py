import pytest

from desktopapptemplate.ui.mainwindow import MainWindow


@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    return window


def test_first(main_window, qtbot):
    assert 1 + 1 == 2
