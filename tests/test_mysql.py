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

    def test_fake_backend_add_datetime_0011(self):
        app_name = 'test_app'
        migration_num = '0011'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_decimal_0012(self):
        app_name = 'test_app'
        migration_num = '0012'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_duration_0013(self):
        app_name = 'test_app'
        migration_num = '0013'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_email_0014(self):
        app_name = 'test_app'
        migration_num = '0014'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_file_0015(self):
        app_name = 'test_app'
        migration_num = '0015'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_filepath_0016(self):
        app_name = 'test_app'
        migration_num = '0016'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_float_0017(self):
        app_name = 'test_app'
        migration_num = '0017'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_generic_ip_0018(self):
        app_name = 'test_app'
        migration_num = '0018'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_null_bool_0019(self):
        app_name = 'test_app'
        migration_num = '0019'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_pos_int_0020(self):
        app_name = 'test_app'
        migration_num = '0020'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_small_pos_int_0021(self):
        app_name = 'test_app'
        migration_num = '0021'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_slug_0022(self):
        app_name = 'test_app'
        migration_num = '0022'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_small_int_0023(self):
        app_name = 'test_app'
        migration_num = '0023'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_text_0024(self):
        app_name = 'test_app'
        migration_num = '0024'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_time_0025(self):
        app_name = 'test_app'
        migration_num = '0025'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_url_0026(self):
        app_name = 'test_app'
        migration_num = '0026'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_uuid_0027(self):
        app_name = 'test_app'
        migration_num = '0027'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_float_0028(self):
        app_name = 'test_app'
        migration_num = '0028'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_unique_together_0029(self):
        app_name = 'test_app'
        migration_num = '0029'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_change_field_name_0030(self):
        app_name = 'test_app'
        migration_num = '0030'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_field_index_0031(self):
        app_name = 'test_app'
        migration_num = '0031'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_drop_field_index_0032(self):
        app_name = 'test_app'
        migration_num = '0032'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_unique_on_field_0033(self):
        app_name = 'test_app'
        migration_num = '0033'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_drop_unique_on_field_0034(self):
        app_name = 'test_app'
        migration_num = '0034'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_add_unique_for_date_0035(self):
        app_name = 'test_app'
        migration_num = '0035'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_drop_unique_for_date_0036(self):
        app_name = 'test_app'
        migration_num = '0036'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_thirdobject_with_pk_0037(self):
        app_name = 'test_app'
        migration_num = '0037'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_rename_table_0038(self):
        app_name = 'test_app'
        migration_num = '0038'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_rename_field_0039(self):
        app_name = 'test_app'
        migration_num = '0039'
        self.assert_sql(app_name=app_name, migration_num=migration_num)

    def test_fake_backend_drop_field_0040(self):
        app_name = 'test_app'
        migration_num = '0040'
        self.assert_sql(app_name=app_name, migration_num=migration_num)
