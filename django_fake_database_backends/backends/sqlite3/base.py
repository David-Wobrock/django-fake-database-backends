from django.db.backends.sqlite3.base import DatabaseWrapper \
    as BaseDatabaseWrapper

from django_fake_database_backends.common.base import DatabaseWrapperMixin
from .schema import DatabaseSchemaEditor


class DatabaseWrapper(DatabaseWrapperMixin, BaseDatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor
