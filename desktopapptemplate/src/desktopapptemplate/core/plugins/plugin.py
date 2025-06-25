class Plugin:
    def __init__(self, name, version):
        self._name = name
        self._version = version

    def name(self):
        return self._name
    
    def version(self):
        return self._version