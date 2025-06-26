from desktopapptemplate.core.plugins.data.dataplugin import DataPlugin


class CsvDataPlugin(DataPlugin):
    def __init__(self):
        super(CsvDataPlugin, self).__init__('csvdataplugin', 'CSV')

    def cols(self):
        if not self.data():
            raise RuntimeError('Data not set')
        return self.data().keys()
    
    def rows(self):
        if not self.data():
            raise RuntimeError('Data not set')        
        return list(self.data().values())[1:] # Assumes header
    
    def nr_cols(self):
        return len(self.cols())
    
    def nr_rows(self):
        return len(self.rows())