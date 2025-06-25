from enum import Enum


class Plugin:
    class Type(Enum):
        DATA = 1
        LOADER = 2
        PROCESSOR = 3
        VIEW = 4

    def __init__(self, name, display_name, type, version):
        self._name = name
        self._display_name = display_name
        self._type = type
        self._version = version

    def name(self):
        return self._name
    
    def display_name(self):
        return self._display_name
    
    def type(self):
        return self._type
    
    def version(self):
        return self._version