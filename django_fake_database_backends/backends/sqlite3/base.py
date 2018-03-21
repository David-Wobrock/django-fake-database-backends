from django.db.backends.sqlite3.base import DatabaseWrapper \
    as BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .fake_db import DatabaseConnection, Cursor
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


class DatabaseWrapper(BaseDatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor
    # Classes instantiated in __init__().
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
