class str(object):
    """String object."""

    def __init__(self, object='', encoding='utf-8', errors='strict'):
        """Construct an immutable string.

        :type object: object
        :type encoding: str
        :type errors: str
        """
        pass

    def __add__(self, y):
        """The concatenation of x and y.

        :type y: str
        :rtype: str
        """
        return ''

    def __mul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: str
        """
        return ''

    def __mod__(self, y):
        """x % y.

        :rtype: str
        """
        return ''

    def __rmul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: str
        """
        return ''

    def __getitem__(self, y):
        """y-th item of x or substring, origin 0.

        :type y: numbers.Integral | slice
        :rtype: str
        """
        return ''

    def __iter__(self):
        """Iterator over bytes.

        :rtype: collections.Iterator[str]
        """
        return []

    def capitalize(self):
        """Return a copy of the string with its first character capitalized
        and the rest lowercased.

        :rtype: str
        """
        return ''

    def center(self, width, fillchar=' '):
        """Return centered in a string of length width.

        :type width: numbers.Integral
        :type fillchar: str
        :rtype: str
        """
        return ''

    def count(self, sub, start=None, end=None):
        """Return the number of non-overlapping occurrences of substring
        sub in the range [start, end].

        :type sub: str
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: int
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'):
        """Return an encoded version of the string as a bytes object.

        :type encoding: str
        :type errors: str
        :rtype: bytes
        """
        return b''

    def endswith(self, suffix, start=None, end=None):
        """Return True if the string ends with the specified suffix,
        otherwise return False.

        :type suffix: str | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        return False

    def find(self, sub, start=None, end=None):
        """Return the lowest index in the string where substring sub is
        found, such that sub is contained in the slice s[start:end].

        :type sub: str
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def format(self, *args, **kwargs):
        """Perform a string formatting operation.

        :rtype: str
        """
        return ''

    def index(self, sub, start=None, end=None):
        """Like find(), but raise ValueError when the substring is not
        found.

        :type sub: str
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def isalnum(self):
        """Return true if all characters in the string are alphanumeric and
        there is at least one character, false otherwise.

        :rtype: bool
        """
        return False

    def isalpha(self):
        """Return true if all characters in the string are alphabetic and there
        is at least one character, false otherwise.

        :rtype: bool
        """
        return False

    def isdigit(self):
        """Return true if all characters in the string are digits and there
        is at least one character, false otherwise.

        :rtype: bool
        """
        return False

    def islower(self):
        """Return true if all cased characters in the string are lowercase
        and there is at least one cased character, false otherwise.

        :rtype: bool
        """
        return False

    def isspace(self):
        """Return true if there are only whitespace characters in the
        string and there is at least one character, false otherwise.

        :rtype: bool
        """
        return False

    def istitle(self):
        """Return true if the string is a titlecased string and there is at
        least one character, for example uppercase characters may only
        follow uncased characters and lowercase characters only cased ones.

        :rtype: bool
        """
        return False

    def isupper(self):
        """Return true if all cased characters in the string are uppercase
        and there is at least one cased character, false otherwise.

        :rtype: bool
        """
        return False

    def join(self, iterable):
        """Return a string which is the concatenation of the strings in the
        iterable.

        :type iterable: collections.Iterable[str]
        :rtype: str
        """
        return ''

    def ljust(self, width, fillchar=' '):
        """Return the string left justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: str
        :rtype: str
        """
        return ''

    def lower(self):
        """Return a copy of the string with all the cased characters
        converted to lowercase.

        :rtype: str
        """
        return ''

    def lstrip(self, chars=None):
        """Return a copy of the string with leading characters removed.

        :type chars: str | None
        :rtype: str
        """
        return ''

    def partition(self, sep):
        """Split the string at the first occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: str
        :rtype: (str, str, str)
        """
        return '', '', ''

    def replace(self, old, new, count=-1):
        """Return a copy of the string with all occurrences of substring
        old replaced by new.

        :type old: str
        :type new: str
        :type count: numbers.Integral
        :rtype: str
        """
        return ''

    def rfind(self, sub, start=None, end=None):
        """Return the highest index in the string where substring sub is
        found, such that sub is contained within s[start:end].

        :type sub: str
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def rindex(self, sub, start=None, end=None):
        """Like rfind(), but raise ValueError when the substring is not
        found.

        :type sub: str
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def rjust(self, width, fillchar=' '):
        """Return the string right justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: str
        :rtype: str
        """
        return ''

    def rpartition(self, sep):
        """Split the string at the last occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: str
        :rtype: (str, str, str)
        """
        return '', '', ''

    def rsplit(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: str | None
        :type maxsplit: numbers.Integral
        :rtype: list[str]
        """
        return []

    def rstrip(self, chars=None):
        """Return a copy of the string with trailing characters removed.

        :type chars: str | None
        :rtype: str
        """
        return ''

    def split(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: str | None
        :type maxsplit: numbers.Integral
        :rtype: list[str]
        """
        return []

    def splitlines(self, keepends=False):
        """Return a list of the lines in the string, breaking at line
        boundaries.

        :type keepends: bool
        :rtype: list[str]
        """
        return []

    def startswith(self, prefix, start=None, end=None):
        """Return True if string starts with the prefix, otherwise return
        False.

        :type prefix: str | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        return False

    def strip(self, chars=None):
        """Return a copy of the string with the leading and trailing
        characters removed.

        :type chars: str | None
        :rtype: str
        """
        return ''

    def swapcase(self):
        """Return a copy of the string with uppercase characters converted
        to lowercase and vice versa.

        :rtype: str
        """
        return ''

    def title(self):
        """Return a titlecased version of the string where words start with
        an uppercase character and the remaining characters are lowercase.

        :rtype: str
        """
        return ''

    def upper(self):
        """Return a copy of the string with all the cased characters
        converted to uppercase.

        :rtype: str
        """
        return ''

    def zfill(self, width):
        """Return the numeric string left filled with zeros in a string of
        length width.

        :type width: numbers.Integral
        :rtype: str
        """
        return ''


class list(object):
    """List object."""

    def __init__(self, iterable=None):
        """Create a list object.

        :type iterable: collections.Iterable[T]
        :rtype: list[T]
        """
        pass

    def __add__(self, y):
        """The concatenation of x and y.

        :type y: list[T]
        :rtype: list[T]
        """
        return []

    def __mul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: list[T]
        """
        return []

    def __rmul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: list[T]
        """
        return []

    def __iter__(self):
        """
        :rtype: collections.Iterator[T]
        """
        return []

    def __getitem__(self, y):
        """y-th item of x or sublist, origin 0.

        :type y: numbers.Integral | slice
        :rtype: T | list[T]
        """
        pass

    def __setitem__(self, i, y):
        """Item i is replaced by y.

        :type i: numbers.Integral
        :type y: T
        :rtype: None
        """
        pass

    def __delitem__(self, i):
        """Remove i-th item.

        :type i: numbers.Integral
        :rtype: None
        """

    def append(self, x):
        """Appends x to the end of the sequence.

        :type x: T
        :rtype: None
        """
        pass

    def extend(self, t):
        """Extends the sequence with the contents of t.

        :type t: collections.Iterable[T]
        :rtype: None
        """
        pass

    def count(self, x):
        """Total number of occurrences of x in the sequence.

        :type x: T
        :rtype: int
        """
        return 0

    def index(self, x, i=None, j=None):
        """Index of the first occurrence of x in the sequence.

        :type x: T
        :type i: numbers.Integral | None
        :type j: numbers.Integral | none
        :rtype: int
        """
        return 0

    def insert(self, i, x):
        """Inserts x into the sequence at the index given by i.

        :type i: numbers.Number
        :type x: T
        :rtype: None
        """
        pass

    def pop(self, i=-1):
        """Retrieves the item at i and also removes it from the sequence.

        :type i: numbers.Number
        :rtype: T
        """
        pass

    def remove(self, x):
        """Remove the first item x from the sequence.

        :type x: T
        :rtype: None
        """
        pass

    def sort(self, cmp=None, key=None, reverse=False):
        """Sort the items of the sequence in place.

        :type cmp: ((T, T) -> int) | None
        :type key: ((T) -> object) | None
        :type reverse: bool
        :rtype: None
        """
        pass