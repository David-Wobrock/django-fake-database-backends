class Cursor(object):
    def execute(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

    def fetchmany(self, *args, **kwargs):
        return []

    def fetchall(self, *args, **kwargs):
        return []


class DatabaseConnection(object):
    def close(self):
        pass

    def cursor(self):
        return Cursor()

    def commit(self):
        pass

    def rollback(self):
        pass
