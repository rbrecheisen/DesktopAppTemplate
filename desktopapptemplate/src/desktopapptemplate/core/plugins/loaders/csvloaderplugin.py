import csv

from collections import defaultdict

from desktopapptemplate.core.plugins.loaders.loaderplugin import LoaderPlugin
from desktopapptemplate.core.plugins.data.csvdataplugin import CsvDataPlugin


class CsvLoaderPlugin(LoaderPlugin):
    def __init__(self):
        super(CsvLoaderPlugin, self).__init__('csvloaderplugin', 'Load CSV')
        self._file_path = None

    def file_path(self):
        return self._file_path
    
    def set_file_path(self, file_path):
        self._file_path = file_path

    def load(self):
        if self.file_path():
            data = defaultdict(list)
            with open(self.file_path(), 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, value in row.items():
                        data[key].append(value)
                csv_data_plugin = CsvDataPlugin()
                csv_data_plugin.set_data(data)
                return csv_data_plugin
        raise RuntimeError('File path not set')