# Hard copy from psycopg2

error_codes_DUPLICATE_DATABASE = '42P04'

class Inet(object):
    def __init__(self, addr):
        self.addr = addr

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.addr)

    def prepare(self, conn):
        self._conn = conn

    def getquoted(self):
        obj = self.addr
        if hasattr(obj, 'prepare'):
            obj.prepare(self._conn)
        return obj.getquoted() + b"::inet"

    def __str__(self):
        return str(self.addr)


def quote_postgre(value):
    return '"{0}"'.format(value)
