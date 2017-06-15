class __coroutine(object):
    """A mock class representing the generator function type."""

    def __init__(self):
        """
        :rtype: __coroutine[V]
        """
        self.__name__ = ''
        self.__qualname__ = ''
        self.cr_await = None
        self.cr_frame = None
        self.cr_running = False
        self.cr_code = None

    def __await__(self):
        """
        :rtype: __generator[unknown, unknown, V]
        """
        return []

    def close(self):
        """
        :rtype: None
        """
        pass

    def send(self, value):
        """
        :rtype: None
        """
        pass

    def throw(self, type, value=None, traceback=None):
        """
        :rtype: None
        """
        pass
