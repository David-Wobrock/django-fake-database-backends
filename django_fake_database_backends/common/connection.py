from .cursor import Cursor


class DatabaseConnection(object):
    data_type_check_constraints = {}
    in_atomic_block = False
    alias = 'default'

    def __init__(self, *args, **kwargs):
        self.ops = kwargs['ops_class'](self) if 'ops_class' in kwargs else None

    def close(self):
        pass

    def cursor(self):
        return Cursor()

    def commit(self):
        pass

    def rollback(self):
        pass

    def set_client_encoding(self, encoding):
        pass
