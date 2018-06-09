import os
import subprocess
import sys
import unittest


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class FakeBackendsTestCase(unittest.TestCase):
    """
    Computes the correct python path,
    executes the sqlmigrate command,
    assert the output to the expected sql...
    """

    TEST_PROJECT_DIR = os.path.join(BASE_DIR, 'test_project/')

    database_backend = 'TODO'

    @classmethod
    def setUpClass(cls):
        super(FakeBackendsTestCase, cls).setUpClass()
        cls.python_exec = '{0}/bin/python'.format(sys.prefix) if hasattr(sys, 'real_prefix') else 'python'
        cls.python_version = sys.version_info.major
        import django
        cls.django_version = '{0}.{1}'.format(*(django.VERSION[:2]))
        cls.django_migrate('mysql_real')
        cls.django_migrate('postgresql_real')

    @classmethod
    def django_migrate(cls, database_alias):
        migrate_cmd = '(cd {0} && {1} manage.py migrate --database {2} --no-input)'.format(
            cls.TEST_PROJECT_DIR, cls.python_exec, database_alias)

        process = subprocess.Popen(
            migrate_cmd,
            shell=True,
            stdout=subprocess.PIPE)
        process.wait()

    def real_sql(self, app_name, migration_num):
        return self._execute_sqlmigrate(
            app_name,
            migration_num,
            '{}_real'.format(self.database_backend))

    def fake_sql(self, app_name, migration_num):
        return self._execute_sqlmigrate(
            app_name,
            migration_num,
            '{}_fake'.format(self.database_backend))

    def _execute_sqlmigrate(self, app_name, migration_num, database_alias):
        sqlmigrate_cmd = '(cd {0} && {1} manage.py sqlmigrate {2} {3} --database {4})'.format(
            self.TEST_PROJECT_DIR, self.python_exec, app_name, migration_num, database_alias)

        process = subprocess.Popen(
            sqlmigrate_cmd,
            shell=True,
            stdout=subprocess.PIPE)
        process.wait()
        self.assertEquals(process.returncode, 0)

        return map(lambda x: x.decode('utf-8'), process.stdout.readlines())

    def assert_sql(self, migration_num, app_name='test_app'):
        expected_sql = self.real_sql(app_name, migration_num)
        fake_backend_sql = self.fake_sql(app_name, migration_num)

        expected_sql = ''.join(expected_sql).replace('\n', '')
        fake_backend_sql = ''.join(fake_backend_sql).replace('\n',  '')
        print('*** Expected output ***')
        print(expected_sql)
        print('*** Gotten output ***')
        print(fake_backend_sql)

        self.assertEqual(expected_sql, fake_backend_sql)
