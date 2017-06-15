class bytes(object):
    """Bytes object."""

    def __init__(self, source='', encoding='utf8', errors='strict'):
        """Construct an immutable array of bytes.

        :type source: object
        :type encoding: str
        :type errors: str
        """
        pass

    def __add__(self, y):
        """The concatenation of x and y.

        :type y: bytes
        :rtype: bytes
        """
        return b''

    def __mul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: bytes
        """
        return b''

    def __rmul__(self, n):
        """n shallow copies of x concatenated.

        :type n: numbers.Integral
        :rtype: bytes
        """
        return b''

    def __getitem__(self, y):
        """y-th item of x or substring, origin 0.

        :type y: numbers.Integral | slice
        :rtype: int | bytes
        """
        return 0

    def __iter__(self):
        """Iterator over bytes.

        :rtype: collections.Iterator[int]
        """
        return []

    def capitalize(self):
        """Return a copy of the string with its first character capitalized
        and the rest lowercased.

        :rtype: bytes
        """
        return b''

    def center(self, width, fillchar=' '):
        """Return centered in a string of length width.

        :type width: numbers.Integral
        :type fillchar: bytes
        :rtype: bytes
        """
        return b''

    def count(self, sub, start=None, end=None):
        """Return the number of non-overlapping occurrences of substring
        sub in the range [start, end].

        :type sub: bytes
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: int
        """
        return 0

    def decode(self, encoding='utf-8', errors='strict'):
        """Return a string decoded from the given bytes.

        :type encoding: str
        :type errors: str
        :rtype: str
        """
        return ''

    def endswith(self, suffix, start=None, end=None):
        """Return True if the string ends with the specified suffix,
        otherwise return False.

        :type suffix: bytes | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        return False

    def find(self, sub, start=None, end=None):
        """Return the lowest index in the string where substring sub is
        found, such that sub is contained in the slice s[start:end].

        :type sub: bytes
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def index(self, sub, start=None, end=None):
        """Like find(), but raise ValueError when the substring is not
        found.

        :type sub: bytes
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

        :type iterable: collections.Iterable[bytes]
        :rtype: bytes
        """
        return b''

    def ljust(self, width, fillchar=' '):
        """Return the string left justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: bytes
        :rtype: bytes
        """
        return b''

    def lower(self):
        """Return a copy of the string with all the cased characters
        converted to lowercase.

        :rtype: bytes
        """
        return b''

    def lstrip(self, chars=None):
        """Return a copy of the string with leading characters removed.

        :type chars: bytes | None
        :rtype: bytes
        """
        return b''

    def partition(self, sep):
        """Split the string at the first occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: bytes
        :rtype: (bytes, bytes, bytes)
        """
        return b'', b'', b''

    def replace(self, old, new, count=-1):
        """Return a copy of the string with all occurrences of substring
        old replaced by new.

        :type old: bytes
        :type new: bytes
        :type count: numbers.Integral
        :rtype: bytes
        """
        return b''

    def rfind(self, sub, start=None, end=None):
        """Return the highest index in the string where substring sub is
        found, such that sub is contained within s[start:end].

        :type sub: bytes
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def rindex(self, sub, start=None, end=None):
        """Like rfind(), but raise ValueError when the substring is not
        found.

        :type sub: bytes
        :type start: numbers.Integral | None
        :type end: numbers.Integral | none
        :rtype: int
        """
        return 0

    def rjust(self, width, fillchar=' '):
        """Return the string right justified in a string of length width.
        Padding is done using the specified fillchar (default is a space).

        :type width: numbers.Integral
        :type fillchar: bytes
        :rtype: bytes
        """
        return b''

    def rpartition(self, sep):
        """Split the string at the last occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself, and the part after the separator.

        :type sep: bytes
        :rtype: (bytes, bytes, bytes)
        """
        return b'', b'', b''

    def rsplit(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: bytes | None
        :type maxsplit: numbers.Integral
        :rtype: list[bytes]
        """
        return []

    def rstrip(self, chars=None):
        """Return a copy of the string with trailing characters removed.

        :type chars: bytes | None
        :rtype: bytes
        """
        return b''

    def split(self, sep=None, maxsplit=-1):
        """Return a list of the words in the string, using sep as the
        delimiter string.

        :type sep: bytes | None
        :type maxsplit: numbers.Integral
        :rtype: list[bytes]
        """
        return []

    def splitlines(self, keepends=False):
        """Return a list of the lines in the string, breaking at line
        boundaries.

        :type keepends: bool
        :rtype: list[bytes]
        """
        return []

    def startswith(self, prefix, start=None, end=None):
        """Return True if string starts with the prefix, otherwise return
        False.

        :type prefix: bytes | tuple
        :type start: numbers.Integral | None
        :type end: numbers.Integral | None
        :rtype: bool
        """
        return False

    def strip(self, chars=None):
        """Return a copy of the string with the leading and trailing
        characters removed.

        :type chars: bytes | None
        :rtype: bytes
        """
        return b''

    def swapcase(self):
        """Return a copy of the string with uppercase characters converted
        to lowercase and vice versa.

        :rtype: bytes
        """
        return b''

    def title(self):
        """Return a titlecased version of the string where words start with
        an uppercase character and the remaining characters are lowercase.

        :rtype: bytes
        """
        return b''

    def upper(self):
        """Return a copy of the string with all the cased characters
        converted to uppercase.

        :rtype: bytes
        """
        return b''

    def zfill(self, width):
        """Return the numeric string left filled with zeros in a string of
        length width.

        :type width: numbers.Integral
        :rtype: bytes
        """
        return b''
