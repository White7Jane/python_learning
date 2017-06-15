class enumerate(object):
    """enumerate object."""

    def __init__(self, iterable, start=0):
        """Create an enumerate object.

        :type iterable: collections.Iterable[T]
        :type start: int | long
        :rtype: enumerate[T]
        """
        pass

    def next(self):
        """Return the next value, or raise StopIteration.

        :rtype: (int, T)
        """
        pass

    def __iter__(self):
        """x.__iter__() <==> iter(x).

        :rtype: collections.Iterator[(int, T)]
        """
        return self
