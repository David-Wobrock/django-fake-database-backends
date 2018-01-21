from django.db.backends.mysql.schema import DatabaseSchemaEditor \
    as BaseDatabaseSchemaEditor
import sys


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
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
        if type(value) == bool:
            return str(int(value))
        # TODO escape correctly all values for mysql
        # Preferably without having the mysql client as dep
        if sys.version_info.major == 3:
            return "b\"'{0}'\"".format(value)
        return "'{0}'".format(value)

    def _field_should_be_indexed(self, model, field):
        create_index = super(
            DatabaseSchemaEditor, self)._field_should_be_indexed(model, field)
        if (create_index and
           field.get_internal_type() == 'ForeignKey' and
           field.db_constraint):
            return False
        return create_index
