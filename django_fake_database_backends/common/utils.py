import django


def split_identifier(identifier):
    """
    Split a SQL identifier into a two element tuple of (namespace, name).
    The identifier could be a table, column, or sequence name might be prefixed
    by a namespace.
    """
    try:
        from django.db.backends.utils import \
            split_identifier as django_split_identifier
        return django_split_identifier(identifier)
    except ImportError:
        try:
            namespace, name = identifier.split('"."')
        except ValueError:
            namespace, name = '', identifier
        return namespace.strip('"'), name.strip('"')


def is_django_2():
    return django.VERSION[0] == 2


def is_django_1():
    return django.VERSION[0] == 1


def is_string(obj):
    if isinstance(obj, str):
        return True

    try:
        return isinstance(obj, unicode)
    except NameError:  # Python3
        return isinstance(obj, bytes)
    return False
