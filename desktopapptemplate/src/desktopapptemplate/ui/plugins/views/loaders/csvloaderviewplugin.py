from desktopapptemplate.ui.plugins.views.loaders.loaderviewplugin import LoaderViewPLugin


class CsvLoaderViewPLugin(LoaderViewPLugin):
    def __init__(self, plugin):
        super(CsvLoaderViewPLugin, self).__init__('csvloaderviewplugin', 'Load CSV', plugin)