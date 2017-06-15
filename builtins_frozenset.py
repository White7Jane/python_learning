class frozenset(object):
    """frozenset object."""

    def __init__(self, iterable=None):
        """Create a frozenset object.

        :type iterable: collections.Iterable[T]
        :rtype: frozenset[T]
        """
        pass

    def copy(self):
        """Return shallow copy of the set.

        :rtype: set[T]
        """
        pass

    def union(self, *other):
        """Return the union of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return frozenset()

    def __or__(self, other):
        """Return the union of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return frozenset()

    def difference(self, *other):
        """Return the difference of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return frozenset()

    def __sub__(self, other):
        """Return the difference of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return frozenset()

    def symmetric_difference(self, other):
        """Return the symmetric difference of this set and another collection as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return frozenset()

    def __xor__(self, other):
        """Return the symmetric difference of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return frozenset()

    def intersection(self, *other):
        """Return the intersection of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return frozenset()

    def __and__(self, other):
        """Return the intersection of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return frozenset()

    def isdisjoint(self, other):
        """Return True if this set and another collection have a null intersection.

        :type other: collections.Iterable[T]
        :rtype: bool
        """
        return False

    def issubset(self, other):
        """Report whether another collection contains this set.

        :type other: collections.Iterable[T]
        :rtype: bool
        """
        return False

    def __le__(self, other):
        """Report whether another set contains this set.

        :type other: collections.Set[T]
        :rtype: bool
        """
        return False

    def __lt__(self, other):
        """Report whether this set is a proper subset of other.

        :type other: collections.Set[T]
        :rtype: bool
        """
        return False

    def issuperset(self, other):
        """Report whether this set contains another collection.

        :type other: collections.Iterable[T]
        :rtype: bool
        """
        return False

    def __ge__(self, other):
        """Report whether this set contains other set.

        :type other: collections.Set[T]
        :rtype: bool
        """
        return False

    def __gt__(self, other):
        """Report whether this set is a proper superset of other.

        :type other: collections.Set[T]
        :rtype: bool
        """
        return False

    def __iter__(self):
        """
        :rtype: collections.Iterator[T]
        """
        pass
