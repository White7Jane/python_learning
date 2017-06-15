class __asyncgenerator(object):
    """A mock class representing the async generator function type."""
    def __init__(self):
        """Create an async generator object.

        :rtype: __asyncgenerator[T, U]
        """
        self.__name__ = ''
        self.__qualname__ = ''
        self.ag_await = None
        self.ag_frame = None
        self.ag_running = False
        self.ag_code = None

    def __aiter__(self):
        """Defined to support iteration over container.

        :rtype: collections.AsyncIterator[T]
        """
        pass

    def __anext__(self):
        """Returns an awaitable, that performs one asynchronous generator
        iteration when awaited.

        :rtype: collections.Awaitable[T]
        """
        pass

    def aclose(self):
        """Returns an awaitable, that throws a GeneratorExit exception
        into generator.

        :rtype: collections.Awaitable[T]
        """
        pass

    def asend(self, value):
        """Returns an awaitable, that pushes the value object in generator.

        :type value: U
        :rtype: collections.Awaitable[T]
        """
        pass

    def athrow(self, type, value=None, traceback=None):
        """Returns an awaitable, that throws an exception into generator.

        :rtype: collections.Awaitable[T]
        """
        pass
