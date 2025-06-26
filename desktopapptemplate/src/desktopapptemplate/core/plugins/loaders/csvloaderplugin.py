from desktopapptemplate.core.plugins.loaders.loaderplugin import LoaderPlugin


class CsvLoaderPlugin(LoaderPlugin):
    def __init__(self):
        super(CsvLoaderPlugin, self).__init__('csvloaderplugin', 'Load CSV')

    def load(self):
        # Use the DataPluginManager to create a new CsvDataPlugin instance
        # and set its data
        pass