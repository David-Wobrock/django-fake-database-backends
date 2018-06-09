from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from django_fake_database_backends.common.schema import (
    DatabaseSchemaEditorMixin,
)
from .utils import quote_postgre


class DatabaseSchemaEditor(
        BaseDatabaseSchemaEditor,
        DatabaseSchemaEditorMixin):

    sql_alter_column_type = ("ALTER COLUMN %(column)s "
                             "TYPE %(type)s USING %(column)s::%(type)s")

    sql_create_sequence = "CREATE SEQUENCE %(sequence)s"
    sql_delete_sequence = "DROP SEQUENCE IF EXISTS %(sequence)s CASCADE"
    sql_set_sequence_max = ("SELECT setval('%(sequence)s', "
                            "MAX(%(column)s)) FROM %(table)s")

    sql_create_index = ("CREATE INDEX %(name)s ON "
                        "%(table)s%(using)s (%(columns)s)%(extra)s")
    sql_create_varchar_index = ("CREATE INDEX %(name)s ON %(table)s "
                                "(%(columns)s varchar_pattern_ops)%(extra)s")
    sql_create_text_index = ("CREATE INDEX %(name)s ON %(table)s "
                             "(%(columns)s text_pattern_ops)%(extra)s")
    sql_delete_index = "DROP INDEX IF EXISTS %(name)s"

    # Setting the constraint to IMMEDIATE runs any deferred checks to allow
    # dropping it in the same transaction.
    sql_delete_fk = ("SET CONSTRAINTS %(name)s IMMEDIATE; "
                     "ALTER TABLE %(table)s DROP CONSTRAINT %(name)s")

    sql_delete_procedure = 'DROP FUNCTION %(procedure)s(%(param_types)s)'

    def quote_value(self, value):
        return quote_postgre(value)
