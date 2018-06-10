from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.mysql.client import DatabaseClient
from django.db.backends.mysql.creation import DatabaseCreation
from django.db.backends.mysql.validation import DatabaseValidation

from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor
from django_fake_database_backends.common import DatabaseConnection, Cursor


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'fake-mysql-database-backend'
    display_name = 'Django Fake MySql Database Backend'

    SchemaEditorClass = DatabaseSchemaEditor

    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = BaseDatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    validation_class = DatabaseValidation

    data_types = {
        'AutoField': 'integer AUTO_INCREMENT',
        'BinaryField': 'longblob',
        'BooleanField': 'bool',
        'CharField': 'varchar(%(max_length)s)',
        'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
        'DateField': 'date',
        'DateTimeField': 'datetime(6)',
        'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
        'DurationField': 'bigint',
        'FileField': 'varchar(%(max_length)s)',
        'FilePathField': 'varchar(%(max_length)s)',
        'FloatField': 'double precision',
        'IntegerField': 'integer',
        'BigIntegerField': 'bigint',
        'IPAddressField': 'char(15)',
        'GenericIPAddressField': 'char(39)',
        'NullBooleanField': 'bool',
        'OneToOneField': 'integer',
        'PositiveIntegerField': 'integer UNSIGNED',
        'PositiveSmallIntegerField': 'smallint UNSIGNED',
        'SlugField': 'varchar(%(max_length)s)',
        'SmallIntegerField': 'smallint',
        'TextField': 'longtext',
        'TimeField': 'time(6)',
        'UUIDField': 'char(32)'
    }

    _limited_data_types = (
        'tinyblob', 'blob', 'mediumblob', 'longblob', 'tinytext', 'text',
        'mediumtext', 'longtext', 'json',
    )

    def get_connection_params(self, *args, **kwargs):
        return {}

    def get_new_connection(self, *args, **kwargs):
        return DatabaseConnection(
            ops_class=DatabaseOperations)

    def _set_autocommit(self, *args, **kwargs):
        pass

    def init_connection_state(self, *args, **kwargs):
        pass

    def create_cursor(self, name=None):
        return Cursor()
