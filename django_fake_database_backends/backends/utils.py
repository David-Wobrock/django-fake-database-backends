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
