from desktopapptemplate.ui.plugins.views.loaders.loaderviewplugin import LoaderViewPlugin


class CsvLoaderViewPLugin(LoaderViewPlugin):
    def __init__(self, name, display_name, version):
        super(CsvLoaderViewPLugin, self).__init__(name, display_name, version)