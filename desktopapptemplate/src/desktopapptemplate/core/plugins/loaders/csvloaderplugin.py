from desktopapptemplate.core.plugins.loaders.loaderplugin import LoaderPlugin


class CsvLoaderPlugin(LoaderPlugin):
    def __init__(self):
        super(CsvLoaderPlugin, self).__init__('csvloaderplugin', 'Load CSV')