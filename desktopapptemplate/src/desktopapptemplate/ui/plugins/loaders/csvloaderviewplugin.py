from desktopapptemplate.ui.plugins.loaders.loaderviewplugin import LoaderViewPlugin


class CsvLoaderViewPlugin(LoaderViewPlugin):
    def __init__(self, plugin):
        super(CsvLoaderViewPlugin, self).__init__('csvloaderviewplugin', 'Load CSV', plugin)