from desktopapptemplate.core.plugins.loaders.loaderplugin import LoaderPlugin


class CsvLoaderPlugin(LoaderPlugin):
    def __init__(self, name, version):
        super(CsvLoaderPlugin, self).__init__(name, version)