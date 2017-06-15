class set(object):
    """Set object."""

    def __init__(self, iterable=None):
        """Create a set object.

        :type iterable: collections.Iterable[T]
        :rtype: set[T]
        """
        pass

    def add(self, x):
        """Add an element x to a set.

        :type x: T
        :rtype: None
        """
        pass

    def discard(self, x):
        """Remove an element x from the set, do nothing if it's not present.

        :type x: T
        :rtype: None
        """
        pass

    def remove(self, x):
        """Remove an element x from the set, raise KeyError if it's not present.

        :type x: T
        :rtype: None
        """
        pass

    def pop(self):
        """Remove and return arbitrary element from the set.

        :rtype: T
        """
        pass

    def copy(self):
        """Return shallow copy of the set.

        :rtype: set[T]
        """
        pass

    def clear(self):
        """Delete all elements from the set.

        :rtype: None
        """
        pass

    def union(self, *other):
        """Return the union of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return set()

    def __or__(self, other):
        """Return the union of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return set()

    def update(self, *other):
        """Update a set with the union of itself and other collections.

        :type other: collections.Iterable[T]
        :rtype: None
        """
        pass

    def difference(self, *other):
        """Return the difference of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return set()

    def __sub__(self, other):
        """Return the difference of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return set()

    def difference_update(self, *other):
        """Remove all elements of other collections from this set.

        :type other: collections.Iterable[T]
        :rtype: None
        """
        pass

    def symmetric_difference(self, other):
        """Return the symmetric difference of this set and another collection as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return set()

    def __xor__(self, other):
        """Return the symmetric difference of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return set()

    def symmetric_difference_update(self, other):
        """Update the set with the symmetric difference of itself and another collection.

        :type other: collections.Iterable[T]
        :rtype: None
        """
        pass

    def intersection(self, *other):
        """Return the intersection of this set and other collections as a new set.

        :type other: collections.Iterable[T]
        :rtype: set[T]
        """
        return set()

    def __and__(self, other):
        """Return the intersection of two sets as a new set.

        :type other: collections.Set[T]
        :rtype: set[T]
        """
        return set()

    def intersection_update(self, *other):
        """Update a set with the intersection of itself and other collections.

        :type other: collections.Iterable[T]
        :rtype: None
        """
        pass

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