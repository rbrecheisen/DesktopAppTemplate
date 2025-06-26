from desktopapptemplate.core.singleton import singleton


@singleton
class PluginManager:
    def __init__(self):
        self._plugins = {}

    def load_plugins(self):
        raise NotImplementedError()

    def all(self):
        return self._plugins.items()
    
    def get(self, name):
        if name in self._plugins.keys():
            return self._plugins[name]
        raise RuntimeError(f'Plugin "{name}" not found')