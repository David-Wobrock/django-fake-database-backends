from django.db.backends.mysql.operations import \
    DatabaseOperations as BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        if name.startswith("`") and name.endswith("`"):
            return name
        return "`%s`" % name
