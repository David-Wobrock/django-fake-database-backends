from django.db.backends.sqlite3.base import DatabaseWrapper \
    as BaseDatabaseWrapper

from .schema import DatabaseSchemaEditor
from django_fake_database_backends.common import DatabaseConnection, Cursor


class DatabaseWrapper(BaseDatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor

    def get_connection_params(self):
        pass

    def get_new_connection(self, *args, **kwargs):
        return DatabaseConnection()

    def create_cursor(self, *args, **kwargs):
        return Cursor()
