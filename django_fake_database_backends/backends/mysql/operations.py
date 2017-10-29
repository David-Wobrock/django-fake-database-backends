from django.db.backends.base.operations import BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        if name.startswith("`") and name.endswith("`"):
            return name
        return "`%s`" % name
