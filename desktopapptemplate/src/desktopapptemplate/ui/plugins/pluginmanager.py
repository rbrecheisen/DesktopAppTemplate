class PluginManager:
    def __init__(self):
        self._plugins = {}

    def load_plugins(self):
        raise NotImplementedError()

    def plugins(self):
        if len(self._plugins.keys()) == 0:
            self._plugins = self.load_plugins()
        return self._plugins.values()
    
    def plugin(self, name):
        if name in self._plugins.keys():
            return self._plugins[name]
        raise RuntimeError(f'Plugin "{name}" not found')