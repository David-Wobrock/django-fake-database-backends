from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection,
)

from django_fake_database_backends.common.introspection import (
    DatabaseIntrospectionMixin,
)


class DatabaseIntrospection(DatabaseIntrospectionMixin,
                            BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        return []

    def get_storage_engine(self, *args, **kwargs):
        return ''
