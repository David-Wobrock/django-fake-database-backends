import django
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.models import ForeignKey
from django_fake_database_backends.backends.utils import split_identifier


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        return []

    def get_storage_engine(self, *args, **kwargs):
        return ''

    def get_constraints(self, model):
        """ Does not connect to any DB,
        instead, compute constraints that should exist"""
        # TODO
        constraints = {}
        for field in model._meta.get_fields():
            is_pk = field.primary_key
            is_fk = type(field) == ForeignKey
            is_unique = field.unique
            has_index = is_pk or is_fk  # or field.db_index  # TODO sure?
            if has_index:
                columns = [field.column]  # TODO handle unique together
                suffix = '_fk_{0}_{1}'.format(
                    split_identifier(
                        field.target_field.model._meta.db_table)[1],
                    field.target_field.column) if is_fk else ''
                constraint_name = \
                    self.connection.schema_editor()._create_index_name(
                        model._meta.db_table if
                        django.VERSION[0] != 1 else model,
                        columns,
                        suffix)

                constraints[constraint_name] = {
                    'columns': columns,
                    'check': False,  # ??
                    'index': has_index,
                    'primary_key': is_pk,
                    'foreign_key': is_fk,
                    'unique': is_unique,
                    'type': 'idx'  # TODO if can do better
                }
        return constraints
