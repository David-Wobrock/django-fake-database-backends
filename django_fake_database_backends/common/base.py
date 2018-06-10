from .connection import DatabaseConnection
from .cursor import Cursor


class DatabaseWrapperMixin(object):
    def get_connection_params(self):
        return {
            'ops_class': self.ops_class
        }

    def get_new_connection(self, conn_params):
        return DatabaseConnection(**conn_params)

    def init_connection_state(self):
        pass

    def create_cursor(self, *args, **kwargs):
        return Cursor()

    def _set_autocommit(self, *args, **kwargs):
        pass
