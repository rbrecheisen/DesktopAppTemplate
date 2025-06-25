from desktopapptemplate.core.plugins.data.dataplugin import DataPlugin


class CsvDataPlugin(DataPlugin):
    def __init__(self, name, display_name, version):
        super(CsvDataPlugin, self).__init__(name, display_name, version)