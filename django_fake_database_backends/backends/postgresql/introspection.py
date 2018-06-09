from django.db.backends.postgresql.introspection import DatabaseIntrospection \
    as BaseDatabaseIntrospection

from django_fake_database_backends.common.introspection import (
    DatabaseIntrospectionMixin,
)


class DatabaseIntrospection(
        BaseDatabaseIntrospection,
        DatabaseIntrospectionMixin):
    pass
