from django.db.backends.base.introspection import BaseDatabaseIntrospection


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        return []

    def get_storage_engine(self, *args, **kwargs):
        return ''
