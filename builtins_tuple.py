class tuple(object):
    """Tuple object."""

    def __add__(self, y):
        """The concatenation of x and y.

        :type y: tuple
        :rtype: tuple
        """
        pass

    def __mul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: tuple
        """
        pass

    def __rmul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: tuple
        """
        pass

    def __getitem__(self, y):
        """y-th item of x or subtuple, origin 0.

        :type y: numbers.Integral | slice
        :rtype: object | tuple | unknown
        """
        pass

    def count(self, x):
        """Total number of occurrences of x in the sequence.

        :type x: object
        :rtype: int
        """
        return 0

    def index(self, x, i=None, j=None):
        """Index of the first occurrence of x in the sequence.

        :type x: object
        :type i: numbers.Integral | None
        :type j: numbers.Integral | none
        :rtype: int
        """
        return 0

    def __iter__(self):
        """
        :rtype: collections.Iterator[object | unknown]
        """
        pass

