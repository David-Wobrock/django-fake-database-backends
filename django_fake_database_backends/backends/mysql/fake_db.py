from .operations import DatabaseOperations


class Cursor:
    def execute(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

    def fetchmany(self, *args, **kwargs):
        return []


class DatabaseConnection:
    data_type_check_constraints = {}
    in_atomic_block = False
    alias = 'default'

    def __init__(self, *args, **kwargs):
        self.ops = DatabaseOperations(self)

    def close(self):
        pass

    def cursor(self):
        return Cursor()
