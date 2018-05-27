class Cursor(object):
    def execute(self, query, vars=None):
        # http://initd.org/psycopg/docs/cursor.html#cursor.query
        self.query = query.encode('utf-8')
        return None

    def close(self, *args, **kwargs):
        pass

    def fetchone(self, *args, **kwargs):
        return None

    def fetchmany(self, *args, **kwargs):
        return []

    def fetchall(self, *args, **kwargs):
        return []
