import datetime
import sys

from django.db.backends.mysql.schema import DatabaseSchemaEditor \
    as BaseDatabaseSchemaEditor

from django_fake_database_backends.common.schema import (
    DatabaseSchemaEditorMixin,
)


class DatabaseSchemaEditor(DatabaseSchemaEditorMixin,
                           BaseDatabaseSchemaEditor):
    def execute(self, sql, params=()):
        sql = str(sql)
        if self.collect_sql:
            ending = "" if sql.endswith(";") else ";"
            if params is not None:
                self.collected_sql.append(
                    (sql % tuple(map(self.quote_value, params))) + ending)
            else:
                self.collected_sql.append(sql + ending)
        # If not collecting the sql, do not execute

    def quote_value(self, value):
        if isinstance(value, bool):
            return str(int(value))
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            if value % 1 == .0:
                return int(value)
            return value
        if self._is_date_or_time(value) and sys.version_info.major == 2:
            return value
        if sys.version_info.major == 3:
            return "b\"'{0}'\"".format(value)
        return "'{0}'".format(value)

    def _is_date_or_time(self, value):
        try:
            datetime.datetime.strptime(value, '%H:%M:%S')
            return True
        except Exception:
            try:
                datetime.datetime.strptime(value, '%Y-%m-%d')
                return True
            except Exception:
                return False

    def _field_should_be_indexed(self, model, field):
        create_index = super(
            DatabaseSchemaEditor, self)._field_should_be_indexed(model, field)
        if (create_index and
           field.get_internal_type() == 'ForeignKey' and
           field.db_constraint):
            return False
        return create_index
