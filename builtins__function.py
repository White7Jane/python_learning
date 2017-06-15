class __function(object):
    """A mock class representing function type."""

    def __init__(self):
        self.__name__ = ''
        self.__doc__ = ''
        self.__dict__ = ''
        self.__module__ = ''

        self.__annotations__ = {}
        self.__defaults__ = {}
        self.__globals__ = {}
        self.__kwdefaults__ = {}
        self.__closure__ = None
        self.__code__ = None

        if sys.version_info >= (3, 3):
            self.__qualname__ = ''
