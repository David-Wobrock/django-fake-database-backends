import collections
import contextlib
import copy

from django.apps.registry import Apps
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor as BaseDatabaseSchemaEditor
from django.db.transaction import atomic


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    def __enter__(self):
        self.deferred_sql = []
        if self.atomic_migration:
            self.atomic = atomic(self.connection.alias)
            self.atomic.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            for sql in self.deferred_sql:
                self.execute(sql)
        if self.atomic_migration:
            self.atomic.__exit__(exc_type, exc_value, traceback)

    '''
    def _remake_table(self, model, create_field=None, delete_field=None, alter_field=None):
        """
        Shortcut to transform a model from old_model into new_model

        The essential steps are:
          1. rename the model's existing table, e.g. "app_model" to "app_model__old"
          2. create a table with the updated definition called "app_model"
          3. copy the data from the old renamed table to the new table
          4. delete the "app_model__old" table
        """
        # Self-referential fields must be recreated rather than copied from
        # the old model to ensure their remote_field.field_name doesn't refer
        # to an altered field.
        def is_self_referential(f):
            return f.is_relation and f.remote_field.model is model
        # Work out the new fields dict / mapping
        body = {
            f.name: f.clone() if is_self_referential(f) else f
            for f in model._meta.local_concrete_fields
        }
        # Since mapping might mix column names and default values,
        # its values must be already quoted.
        mapping = {f.column: self.quote_name(f.column) for f in model._meta.local_concrete_fields}
        mapping = collections.OrderedDict(sorted(mapping.items()))
        # This maps field names (not columns) for things like unique_together
        rename_mapping = {}
        # If any of the new or altered fields is introducing a new PK,
        # remove the old one
        restore_pk_field = None
        if getattr(create_field, 'primary_key', False) or (
                alter_field and getattr(alter_field[1], 'primary_key', False)):
            for name, field in list(body.items()):
                if field.primary_key:
                    field.primary_key = False
                    restore_pk_field = field
                    if field.auto_created:
                        del body[name]
                        del mapping[field.column]
        # Add in any created fields
        if create_field:
            body[create_field.name] = create_field
            # Choose a default and insert it into the copy map
            if not create_field.many_to_many and create_field.concrete:
                mapping[create_field.column] = self.quote_value(
                    self.effective_default(create_field)
                )
        # Add in any altered fields
        if alter_field:
            old_field, new_field = alter_field
            body.pop(old_field.name, None)
            mapping.pop(old_field.column, None)
            body[new_field.name] = new_field
            if old_field.null and not new_field.null:
                case_sql = "coalesce(%(col)s, %(default)s)" % {
                    'col': self.quote_name(old_field.column),
                    'default': self.quote_value(self.effective_default(new_field))
                }
                mapping[new_field.column] = case_sql
            else:
                mapping[new_field.column] = self.quote_name(old_field.column)
            rename_mapping[old_field.name] = new_field.name
        # Remove any deleted fields
        if delete_field:
            del body[delete_field.name]
            del mapping[delete_field.column]
            # Remove any implicit M2M tables
            if delete_field.many_to_many and delete_field.remote_field.through._meta.auto_created:
                return self.delete_model(delete_field.remote_field.through)
        # Work inside a new app registry
        apps = Apps()

        # Provide isolated instances of the fields to the new model body so
        # that the existing model's internals aren't interfered with when
        # the dummy model is constructed.
        body = copy.deepcopy(body)

        # Work out the new value of unique_together, taking renames into
        # account
        unique_together = [
            [rename_mapping.get(n, n) for n in unique]
            for unique in model._meta.unique_together
        ]

        # Work out the new value for index_together, taking renames into
        # account
        index_together = [
            [rename_mapping.get(n, n) for n in index]
            for index in model._meta.index_together
        ]

        indexes = model._meta.indexes
        if delete_field:
            indexes = [
                index for index in indexes
                if delete_field.name not in index.fields
            ]

        # Construct a new model for the new state
        meta_contents = {
            'app_label': model._meta.app_label,
            'db_table': model._meta.db_table,
            'unique_together': unique_together,
            'index_together': index_together,
            'indexes': indexes,
            'apps': apps,
        }
        meta = type("Meta", (), meta_contents)
        body['Meta'] = meta
        body['__module__'] = model.__module__

        temp_model = type(model._meta.object_name, model.__bases__, body)

        # We need to modify model._meta.db_table, but everything explodes
        # if the change isn't reversed before the end of this method. This
        # context manager helps us avoid that situation.
        @contextlib.contextmanager
        def altered_table_name(model, temporary_table_name):
            original_table_name = model._meta.db_table
            model._meta.db_table = temporary_table_name
            yield
            model._meta.db_table = original_table_name

        with altered_table_name(model, model._meta.db_table + "__old"):
            # Rename the old table to make way for the new
            self.alter_db_table(
                model, temp_model._meta.db_table, model._meta.db_table,
                disable_constraints=False,
            )
            # Create a new table with the updated schema.
            self.create_model(temp_model)

            # Copy data from the old table into the new table
            field_maps = list(mapping.items())
            self.execute("INSERT INTO %s (%s) SELECT %s FROM %s" % (
                self.quote_name(temp_model._meta.db_table),
                ', '.join(self.quote_name(x) for x, y in field_maps),
                ', '.join(y for x, y in field_maps),
                self.quote_name(model._meta.db_table),
            ))

            # Delete the old table
            self.delete_model(model, handle_autom2m=False)

        # Run deferred SQL on correct table
        for sql in self.deferred_sql:
            self.execute(sql)
        self.deferred_sql = []
        # Fix any PK-removed field
        if restore_pk_field:
            restore_pk_field.primary_key = True
    '''
