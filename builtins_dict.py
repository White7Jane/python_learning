class dict(object):
    """Dictionary object."""

    def __init__(self, iterable=None, **kwargs):
        """Create a dictionary object.

        :type iterable: collections.Iterable[(T, V)]
        :rtype: dict[T, V]
        """
        pass

    def __iter__(self):
        """
        :rtype: collections.Iterator[T]
        """
        pass

    def __len__(self):
        """Return the number of items in the dictionary d.

        :rtype: int
        """
        return 0

    def __getitem__(self, key):
        """Return the item of d with key key.

        :type key: T
        :rtype: V
        """
        pass

    def __setitem__(self, key, value):
        """Set d[key] to value.

        :type key: T
        :type value: V
        :rtype: None
        """
        pass

    def __delitem__(self, key):
        """Remove d[key] from d.

        :type key: T
        :rtype: None
        """
        pass

    def copy(self):
        """Return a shallow copy of the dictionary.

        :rtype: dict[T, V]
        """
        return self

    @staticmethod
    def fromkeys(seq, value=None):
        """Create a new dictionary with keys from seq and values set to value.

        :type seq: collections.Iterable[T]
        :type value: V
        :rtype: dict[T, V]
        """
        return {}

    def get(self, key, default=None):
        """Return the value for key if key is in the dictionary, else default.

        :type key: T
        :type default: V | None
        :rtype: V
        """
        pass

    def items(self):
        """Return a copy of the dictionary's list of (key, value) pairs.

        :rtype: collections.Iterable[(T, V)]
        """
        return []

    def keys(self):
        """Return a copy of the dictionary's list of keys.

        :rtype: collections.Iterable[T]
        """
        return []

    def pop(self, key, default=None):
        """If key is in the dictionary, remove it and return its value, else
        return default.

        :type key: T
        :type default: V | None
        :rtype: V
        """
        pass

    def popitem(self):
        """Remove and return an arbitrary (key, value) pair from the
        dictionary.

        :rtype: (T, V)
        """
        pass

    def setdefault(self, key, default=None):
        """If key is in the dictionary, return its value.

        :type key: T
        :type default: V | None
        :rtype: V
        """
        pass

    def update(self, other=None, **kwargs):
        """Update the dictionary with the key/value pairs from other,
        overwriting existing keys.

        :type other: dict[T, V] | collections.Iterable[(T, V)]
        :rtype: None
        """
        pass

    def values():
        """Return a copy of the dictionary's list of values.

        :rtype: collections.Iterable[V]
        """
        return []
