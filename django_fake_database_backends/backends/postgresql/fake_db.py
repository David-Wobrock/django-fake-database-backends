class Cursor(object):
    def execute(self, query, vars=None):
        # http://initd.org/psycopg/docs/cursor.html#cursor.query
        self.query = query.encode('utf-8')
        return None

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

    def set_client_encoding(self, encoding):
        pass
