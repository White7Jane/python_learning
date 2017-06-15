def abs(number):
    """Return the absolute value of the argument.

    :type number: T
    :rtype: T | unknown
    """
    return number


def all(iterable):
    """Return True if bool(x) is True for all values x in the iterable.

    :type iterable: collections.Iterable
    :rtype: bool
    """
    return False


def any(iterable):
    """Return True if bool(x) is True for any x in the iterable.

    :type iterable: collections.Iterable
    :rtype: bool
    """
    return False


def bin(number):
    """Return the binary representation of an integer or long integer.

    :type number: numbers.Number
    :rtype: str
    """
    return ''


def callable(object):
    """Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances with a __call__() method.

    :rtype: bool
    """
    return False


def chr(i):
    """Return a string of one character with ordinal i; 0 <= i < 256.

    :type i: numbers.Integral
    :rtype: str
    """
    return ''


def dir(object=None):
    """If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the
    attributes of the given object, and of attributes reachable from it.

    :rtype: list[str]
    """
    return []


def divmod(x, y):
    """Return the tuple ((x-x%y)/y, x%y).

    :type x: numbers.Number
    :type y: numbers.Number
    :rtype: (int | long | float | unknown, int | long | float | unknown)
    """
    return 0, 0


def filter(function_or_none, sequence):
    """Return those items of sequence for which function(item) is true. If
    function is None, return the items that are true. If sequence is a tuple
    or string, return the same type, else return a list.

    :type function_or_none: collections.Callable | None
    :type sequence: T <= list | collections.Iterable | bytes | str
    :rtype: T
    """
    return sequence


def getattr(object, name, default=None):
    """Get a named attribute from an object; getattr(x, 'y') is equivalent to
    x.y. When a default argument is given, it is returned when the attribute
    doesn't exist; without it, an exception is raised in that case.

    :type name: str
    """
    pass


def globals():
    """Return the dictionary containing the current scope's global variables.

    :rtype: dict[str, unknown]
    """
    return {}


def hasattr(object, name):
    """Return whether the object has an attribute with the given name.

    :type name: str
    :rtype: bool
    """
    return False


def hash(object):
    """Return a hash value for the object.

    :rtype: int
    """
    return 0


def hex(number):
    """Return the hexadecimal representation of an integer or long integer.

    :type number: numbers.Integral
    :rtype: str
    """
    return ''


def id(object):
    """Return the identity of an object.

    :rtype: int
    """
    return 0


def isinstance(object, class_or_type_or_tuple):
    """Return whether an object is an instance of a class or of a subclass
    thereof.

    :rtype: bool
    """
    return False


def issubclass(C, B):
    """Return whether class C is a subclass (i.e., a derived class) of class B.

    :rtype: bool
    """
    return False


def iter(object, sentinel=None):
    """Get an iterator from an object. In the first form, the argument must
    supply its own iterator, or be a sequence. In the second form, the callable
    is called until it returns the sentinel.

    :type object: collections.Iterable[T] | (() -> object)
    :type sentinel: object | None
    :rtype: collections.Iterator[T]
    """
    return []


def len(object):
    """Return the number of items of a sequence or mapping.

    :type object: collections.Sized
    :rtype: int
    """
    return 0


def locals():
    """Update and return a dictionary containing the current scope's local
    variables.

    :rtype: dict[str, unknown]
    """
    return {}


def max(*args, key=None, default=None):
    """Return the largest item in an iterable or the largest of two or more
    arguments.

    :rtype: object | unknown
    """
    pass


def map(function, sequence, *sequence_1):
    """Return a list of the results of applying the function to the items of
    the argument sequence(s).

    :type function: ((T) -> V) | None
    :type sequence: collections.Iterable[T]
    :rtype: list[V] | bytes | str
    """
    pass


def min(*args, key=None, default=None):
    """Return the smallest item in an iterable or the smallest of two or more
    arguments.

    :rtype: object | unknown
    """
    pass


def next(iterator, default=None):
    """Return the next item from the iterator.

    :type iterator: collections.Iterator[T]
    :rtype: T
    """
    pass


def oct(number):
    """Return the octal representation of an integer or long integer.

    :type number: numbers.Integral
    :rtype: str
    """
    return ''


def open(name, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
         closefd=None, opener=None):
    """Open a file, returns a file object.

    :type name: str | os.PathLike
    :type mode: str
    :type buffering: numbers.Integral
    :type encoding: str | None
    :type errors: str | None
    :rtype: file
    """
    return file()


def ord(c):
    """Return the integer ordinal of a one-character string.

    :type c: bytes | str
    :rtype: int
    """
    return 0


def pow(x, y, z=None):
    """With two arguments, equivalent to x**y. With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).

    :type x: numbers.Number
    :type y: numbers.Number
    :type z: numbers.Number | None
    :rtype: int | long | float | complex
    """
    return 0


def print(*objects, sep=' ', end='\n', file=None, flush=False):
    """Print objects to the stream file, separated by sep and followed by end.

    :type sep: str
    :type end: str
    :type flush: bool
    :rtype: None
    """
    pass


def repr(object):
    """
    Return the canonical string representation of the object.

    :rtype: str
    """
    return ''


def round(number, ndigits=None):
    """Round a number to a given precision in decimal digits (default 0 digits).

    :type number: object
    :type ndigits: numbers.Integral | None
    :rtype: float
    """
    return 0.0


def vars(object=None):
    """Without arguments, equivalent to locals(). With an argument, equivalent
    to object.__dict__.

    :rtype: dict[str, unknown]
    """
    return {}


