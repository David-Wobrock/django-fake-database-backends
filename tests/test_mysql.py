import unittest
import subprocess
from tests.testcases import FakeBackendsTestCase


class MySqlTest(FakeBackendsTestCase):
    database_backend = 'mysql'

    def test_cannot_migrate(self):
        cmd = '(cd {0} && {1} manage.py migrate)'.format(self.TEST_PROJECT_DIR, self.python_exec)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertNotEqual(process.returncode, 0)
        # TODO assert that some message is displayed

    @unittest.skip("todo")
    def test_show_warning_runserver(self):
        cmd = '(cd {0} && {1} manage.py runserver)'.format(self.TEST_PROJECT_DIR, self.python_exec)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        # TODO assert that an error happenend + some message is displayed

    def test_fake_backend_create_table_0001(self):
        app_name = 'test_app'
        migration_num = '0001'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_create_table_with_field_0002(self):
        app_name = 'test_app'
        migration_num = '0002'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_not_null_field_0003(self):
        app_name = 'test_app'
        migration_num = '0003'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_drop_field_0004(self):
        app_name = 'test_app'
        migration_num = '0004'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_alter_field_0005(self):
        app_name = 'test_app'
        migration_num = '0005'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_big_int_0006(self):
        app_name = 'test_app'
        migration_num = '0006'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_binary_0007(self):
        app_name = 'test_app'
        migration_num = '0007'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_boolean_0008(self):
        app_name = 'test_app'
        migration_num = '0008'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_char_0009(self):
        app_name = 'test_app'
        migration_num = '0009'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_date_0010(self):
        app_name = 'test_app'
        migration_num = '0010'
        self.assert_sql(app_name=app_name, migration_num=migration_num)
