from desktopapptemplate.ui.plugins.loaders.loaderviewplugin import LoaderViewPlugin
from desktopapptemplate.ui.components.csvloaderdialog import CsvLoaderDialog


class CsvLoaderViewPlugin(LoaderViewPlugin):
    def __init__(self, plugin):
        super(CsvLoaderViewPlugin, self).__init__('csvloaderviewplugin', 'Load CSV', plugin)
        self._dialog = None
    
    def dialog(self):
        if not self._dialog:
            self._dialog = CsvLoaderDialog(self)
        return self._dialog
    
    def show(self):
        if self.dialog():
            result = self.dialog().exec()
            if result == 1:
                file_path = self.dialog().file_path()
                # We now have a valid CSV file path
                # Create a new CsvDataPlugin from it by loading the CSV data from file
                # using the CsvLoaderPlugin. Then add this data to the data manager for
                # easy access later.
                print(file_path)