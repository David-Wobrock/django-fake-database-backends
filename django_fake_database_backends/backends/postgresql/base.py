from django.db.backends.base.base import BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .fake_db import DatabaseConnection, Cursor
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'fake-postgresql-database-backend'
    display_name = 'Django Fake PostgreSQL Database Backend'

    SchemaEditorClass = DatabaseSchemaEditor

    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    def get_connection_params(self):
        pass

    def get_new_connection(self, *args, **kwargs):
        return DatabaseConnection()

    def create_cursor(self, *args, **kwargs):
        return Cursor()

    def _set_autocommit(self, autocommit):
        with self.wrap_database_errors:
            self.connection.autocommit = autocommit

    def init_connection_state(self):
        self.connection.set_client_encoding('UTF8')

        timezone_changed = self.ensure_timezone()
        if timezone_changed:
            # Commit after setting the time zone (see #17062)
            if not self.get_autocommit():
                self.connection.commit()
