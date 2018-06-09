import django

from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.models import ForeignKey

from django_fake_database_backends.common.introspection import DatabaseIntrospectionMixin
from .utils import split_identifier


class DatabaseIntrospection(BaseDatabaseIntrospection, DatabaseIntrospectionMixin):
    def get_table_list(self, cursor):
        return []

    def get_storage_engine(self, *args, **kwargs):
        return ''
