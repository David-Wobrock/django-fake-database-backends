import os
import unittest
import subprocess

TEST_PROJECT_DIR = os.path.join(os.path.dirname(__file__), 'test_project/')

class MySqlTest(unittest.TestCase):
    def test_sqlgeneration_create_table(self):
        cmd = '(cd {0} && python manage.py sqlmigrate test_app 0001)'.format(TEST_PROJECT_DIR)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertEqual(process.returncode, 0)

        contains_create_table = any(x.strip() == 'CREATE TABLE `test_app_a` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `null_field` integer NULL);' for x in process.stdout)
        self.assertTrue(contains_create_table)

    def test_sqlgeneration_add_not_null_field(self):
        cmd = '(cd {0} && python manage.py sqlmigrate test_app 0002)'.format(TEST_PROJECT_DIR)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertEqual(process.returncode, 0)

        contains_add_column = any(x.strip() == 'ALTER TABLE `test_app_a` ADD COLUMN `new_not_null_field` integer DEFAULT 1 NOT NULL;' for x in process.stdout)
        contains_drop_default = any(x.strip() == 'ALTER TABLE `test_app_a` ALTER COLUMN `new_not_null_field` DROP DEFAULT;' for x in process.stdout)
        self.assertTrue(contains_add_column)
        self.assertTrue(contains_drop_default)

    def test_cannot_migrate(self):
        cmd = '(cd {0} && python manage.py migrate)'.format(TEST_PROJECT_DIR)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertNotEqual(process.returncode, 0)

    #def test_show_warning_runserver(self):
        #cmd = '(cd {0} && python manage.py runserver)'.format(TEST_PROJECT_DIR)
        #process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        #process.wait()

        # TODO
