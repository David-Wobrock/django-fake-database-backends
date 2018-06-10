from .utils import is_django_2, is_string


class DatabaseSchemaEditorMixin(object):
    def _constraint_names(self, model, column_names=None, unique=None,
                          primary_key=None, index=None, foreign_key=None,
                          check=None, type_=None):
        """Return all constraint names matching the columns and conditions."""
        if column_names is not None:
            column_names = [
                self.connection.introspection.column_name_converter(name)
                for name in column_names
            ]

        constraints = self.connection.introspection.get_constraints(model)

        result = []
        for name, infodict in constraints.items():
            if column_names is None or column_names == infodict['columns']:
                if unique is not None and infodict['unique'] != unique:
                    continue
                if primary_key is not None and \
                        infodict['primary_key'] != primary_key:
                    continue
                if index is not None and infodict['index'] != index:
                    continue
                if check is not None and infodict['check'] != check:
                    continue
                if foreign_key is not None and not infodict['foreign_key']:
                    continue
                if type_ is not None and infodict['type'] != type_:
                    continue
                result.append(name)
        return result

    def _create_index_name(self, model_or_table_name, *args, **kwargs):
        if is_django_2() and not is_string(model_or_table_name):
            model_or_table_name = model_or_table_name._meta.db_table
        return super(DatabaseSchemaEditorMixin, self)._create_index_name(
            model_or_table_name, *args, **kwargs)
