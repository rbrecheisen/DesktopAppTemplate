import os

from desktopapptemplate.core.plugins.loaders.loaderpluginmanager import LoaderPluginManager
from desktopapptemplate.core.plugins.data.csvdataplugin import CsvDataPlugin


TEST_DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


def test_load_csv_data():
    loader = LoaderPluginManager().get('csvloaderplugin')
    loader.set_file_path(os.path.join(TEST_DATA_DIR, 'data.csv'))
    data = loader.load()
    assert data
    assert isinstance(data, CsvDataPlugin)
    assert data.nr_rows() == 2
    assert data.nr_cols() == 3