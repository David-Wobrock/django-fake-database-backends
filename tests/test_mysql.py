import os
import unittest
import subprocess


TEST_PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test_project/')


class MySqlTest(unittest.TestCase):
    def _assert_sqlmigrate_result(self, project_path, app_name='test_app', migration_num='0001', expected_migration_content=None):
        assert expected_migration_content is not None
        cmd = '(cd {0} && python manage.py sqlmigrate {1} {2})'.format(project_path, app_name, migration_num)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertEqual(process.returncode, 0)
        self.assertEqual(
            ''.join(map(lambda x: x.decode('utf-8'), process.stdout.readlines())).replace('\n', ''),
            expected_migration_content.replace('\n', ''))

    def _assert_sqlmigrate_fails(self, project_path, app_name='test_app', migration_num='0001'):
        cmd = '(cd {0} && python manage.py sqlmigrate {1} {2})'.format(project_path, app_name, migration_num)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertEqual(process.returncode, 1)


    def test_cannot_migrate(self):
        cmd = '(cd {0} && python manage.py migrate)'.format(TEST_PROJECT_DIR)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

        self.assertNotEqual(process.returncode, 0)

    @unittest.skip("todo")
    def test_show_warning_runserver(self):
        cmd = '(cd {0} && python manage.py runserver)'.format(TEST_PROJECT_DIR)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()

    def test_sqlgeneration_create_table_0001(self):
        migration_num = '0001'
        expected_sql = """
BEGIN;
--
-- Create model A
--
CREATE TABLE `test_app_a` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `null_field` integer NULL);

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_add_not_null_field_0002(self):
        migration_num = '0002'
        expected_sql = """
BEGIN;
--
-- Add field new_not_null_field to a
--
ALTER TABLE `test_app_a` ADD COLUMN `new_not_null_field` integer DEFAULT 1 NOT NULL;
ALTER TABLE `test_app_a` ALTER COLUMN `new_not_null_field` DROP DEFAULT;

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_add_not_null_field_preserve_default_0003(self):
        migration_num = '0003'
        expected_sql = """
BEGIN;
--
-- Add field new_not_null_field_preserve_default to a
--
ALTER TABLE `test_app_a` ADD COLUMN `new_not_null_field_preserve_default` integer DEFAULT 0 NOT NULL;
ALTER TABLE `test_app_a` ALTER COLUMN `new_not_null_field_preserve_default` DROP DEFAULT;

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_drop_field_0004(self):
        migration_num = '0004'
        expected_sql = """
BEGIN;
--
-- Remove field new_not_null_field_preserve_default from a
--
ALTER TABLE `test_app_a` DROP COLUMN `new_not_null_field_preserve_default`;

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_add_lots_of_fields_0005(self):
        migration_num = '0005'
        expected_sql = """
BEGIN;
--
-- Add field mybiginteger to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mybiginteger` bigint NULL;
--
-- Add field mybinary to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mybinary` longblob NULL;
--
-- Add field myboolean to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myboolean` bool DEFAULT 0 NOT NULL;
ALTER TABLE `test_app_a` ALTER COLUMN `myboolean` DROP DEFAULT;
--
-- Add field mychar to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mychar` varchar(256) NULL;
--
-- Add field mydecimal to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mydecimal` numeric(20, 5) NULL;
--
-- Add field myduration to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myduration` bigint NULL;
--
-- Add field myemail to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myemail` varchar(254) NULL;
--
-- Add field myfile to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myfile` varchar(100) NULL;
--
-- Add field myfilepath to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myfilepath` varchar(100) NULL;
--
-- Add field myfloat to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myfloat` double precision NULL;
--
-- Add field mygenericipaddress to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mygenericipaddress` char(39) DEFAULT 8.8.8.8 NOT NULL;
ALTER TABLE `test_app_a` ALTER COLUMN `mygenericipaddress` DROP DEFAULT;
--
-- Add field myimage to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myimage` varchar(100) NULL;
--
-- Add field mynullboolean to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mynullboolean` bool NULL;
--
-- Add field mypositiveinteger to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mypositiveinteger` integer UNSIGNED DEFAULT 5 NOT NULL;
ALTER TABLE `test_app_a` ALTER COLUMN `mypositiveinteger` DROP DEFAULT;
--
-- Add field mypositivesmallinteger to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mypositivesmallinteger` smallint UNSIGNED NULL;
--
-- Add field myslug to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myslug` varchar(50) NULL;
--
-- Add field mytext to a
--
ALTER TABLE `test_app_a` ADD COLUMN `mytext` longtext NOT NULL UNIQUE;
UPDATE `test_app_a` SET `mytext` = Test text;
--
-- Add field myurl to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myurl` varchar(200) NULL;
--
-- Add field myuuid to a
--
ALTER TABLE `test_app_a` ADD COLUMN `myuuid` char(32) NULL UNIQUE;
CREATE INDEX `test_app_a_myslug_c270affb` ON `test_app_a` (`myslug`);
COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_add_unique_together_0006(self):
        migration_num = '0006'
        expected_sql = """

BEGIN;
--
-- Alter unique_together for a (1 constraint(s))
--
ALTER TABLE `test_app_a` ADD CONSTRAINT test_app_a_null_field_new_not_null_field_470b5a0c_uniq UNIQUE (`null_field`, `new_not_null_field`);

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)


    def test_sqlgeneration_incoherent_0007(self):
        migration_num = '0007'
        self._assert_sqlmigrate_fails(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num)

    def test_sqlgeneration_create_table_and_all_relations_0008(self):
        migration_num = '0008'
        expected_sql = """
BEGIN;
--
-- Create model NewClass
--
CREATE TABLE `test_app_newclass` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `mya_id` integer NOT NULL UNIQUE, `myafk_id` integer NULL, `myafkprotect_id` integer NULL, `myaname_id` integer NULL UNIQUE);
--
-- Add field mynewclass to a
--
CREATE TABLE `test_app_a_mynewclass` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `a_id` integer NOT NULL, `newclass_id` integer NOT NULL);
ALTER TABLE `test_app_newclass` ADD CONSTRAINT `test_app_newclass_mya_id_5e635c44_fk_test_app_a_id` FOREIGN KEY (`mya_id`) REFERENCES `test_app_a` (`id`);
ALTER TABLE `test_app_newclass` ADD CONSTRAINT `test_app_newclass_myafk_id_55edb7fa_fk_test_app_a_id` FOREIGN KEY (`myafk_id`) REFERENCES `test_app_a` (`id`);
ALTER TABLE `test_app_newclass` ADD CONSTRAINT `test_app_newclass_myafkprotect_id_12c7d975_fk_test_app_a_id` FOREIGN KEY (`myafkprotect_id`) REFERENCES `test_app_a` (`id`);
ALTER TABLE `test_app_newclass` ADD CONSTRAINT `test_app_newclass_myaname_id_032df7a2_fk_test_app_a_id` FOREIGN KEY (`myaname_id`) REFERENCES `test_app_a` (`id`);
ALTER TABLE `test_app_a_mynewclass` ADD CONSTRAINT `test_app_a_mynewclass_a_id_651aa63d_fk_test_app_a_id` FOREIGN KEY (`a_id`) REFERENCES `test_app_a` (`id`);
ALTER TABLE `test_app_a_mynewclass` ADD CONSTRAINT `test_app_a_mynewclas_newclass_id_f67c181f_fk_test_app_` FOREIGN KEY (`newclass_id`) REFERENCES `test_app_newclass` (`id`);
ALTER TABLE `test_app_a_mynewclass` ADD CONSTRAINT test_app_a_mynewclass_a_id_newclass_id_2cdacc51_uniq UNIQUE (`a_id`, `newclass_id`);
COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    @unittest.skip("todo")
    def test_sqlgeneration_TODO_0009(self):
        migration_num = '0009'
        expected_sql = ""
        self.fail('is missing')
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_create_index_0010(self):
        migration_num = '0010'
        expected_sql = """
BEGIN;
--
-- Alter field new_not_null_field on a
--
CREATE INDEX `test_app_a_new_not_null_field_c06cff38` ON `test_app_a` (`new_not_null_field`);

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    def test_sqlgeneration_drop_index_0011(self):
        migration_num = '0011'
        expected_sql = """
BEGIN;
--
-- Alter field new_not_null_field on a
--

COMMIT;
"""
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)

    @unittest.skip("todo")
    def test_sqlgeneration_TODO_0012(self):
        migration_num = '0012'
        expected_sql = ""
        self.fail('is missing')
        self._assert_sqlmigrate_result(
            project_path=TEST_PROJECT_DIR,
            migration_num=migration_num, 
            expected_migration_content=expected_sql)
