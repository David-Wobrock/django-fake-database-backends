from django.db.backends.mysql.schema import DatabaseSchemaEditor \
    as BaseDatabaseSchemaEditor


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
        # TODO escape correctly all values for mysql
        # Preferably without having the mysql client as dep
        return value
