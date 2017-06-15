class type(object):
    """Type of object."""

    def __instancecheck__(cls, instance):
        """Return true if instance should be considered a (direct or indirect)
        instance of class.
        """
        return False

    def __subclasscheck__(cls, subclass):
        """Return true if subclass should be considered a (direct or indirect)
        subclass of class.
        """
        return False

    @staticmethod
    def __prepare__(metacls, name, bases):
        """Used to create the namespace for the class statement.

        :rtype: dict[str, unknown]
        """
        return {}
