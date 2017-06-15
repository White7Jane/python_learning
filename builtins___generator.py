class __generator(object):
    """A mock class representing the generator function type."""
    def __init__(self):
        """Create a generator object.

        :rtype: __generator[T, U, V]
        """
        self.gi_code = None
        self.gi_frame = None
        self.gi_running = 0

    def __iter__(self):
        """Defined to support iteration over container.

        :rtype: collections.Iterator[T]
        """
        pass

    def __next__(self):
        """Return the next item from the container.

        :rtype: T
        """
        pass

    def close(self):
        """Raises new GeneratorExit exception inside the generator to
        terminate the iteration.

        :rtype: None
        """
        pass

    def send(self, value):
        """Resumes the generator and "sends" a value that becomes the
        result of the current yield-expression.

        :type value: U
        :rtype: None
        """
        pass

    def throw(self, type, value=None, traceback=None):
        """Used to raise an exception inside the generator.

        :rtype: None
        """
        pass
