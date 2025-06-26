from desktopapptemplate.core.plugins.data.dataplugin import DataPlugin


class CsvDataPlugin(DataPlugin):
    def __init__(self):
        super(CsvDataPlugin, self).__init__('csvdataplugin', 'CSV')