import unittest
from tests.utils import order_insert_statements


class TestUtilsTest(unittest.TestCase):
    def test_nothing_changed(self):
        sql = [
            'BEGIN;',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 3)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], sql[2])

    def test_insert_values_statement(self):
        sql = [
            'BEGIN;',
            '--',
            'INSERT INTO "table" ("id", "foo", "bar") VALUES (1, NULL, "val");',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 5)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], 'INSERT INTO "table" ("bar", "foo", "id") VALUES ("val", NULL, 1);')
        self.assertEqual(ordered_sql[3], sql[3])
        self.assertEqual(ordered_sql[4], sql[4])

    def test_insert_values_one_column_statement(self):
        sql = [
            'BEGIN;',
            '--',
            'INSERT INTO "table" ("id") VALUES (1);',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 5)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], sql[2])
        self.assertEqual(ordered_sql[3], sql[3])
        self.assertEqual(ordered_sql[4], sql[4])

    def test_insert_select_statement(self):
        sql = [
            'BEGIN;',
            '--',
            'INSERT INTO "table" ("id", "foo", "bar") SELECT 1, NULL, "val" FROM "table2";',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 5)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], 'INSERT INTO "table" ("bar", "foo", "id") SELECT "val", NULL, 1 FROM "table2";')
        self.assertEqual(ordered_sql[3], sql[3])
        self.assertEqual(ordered_sql[4], sql[4])

    def test_multiple_insert_statements(self):
        sql = [
            'BEGIN;',
            '--',
            'INSERT INTO "table" ("id", "foo", "bar") VALUES (1, NULL, "val");',
            'INSERT INTO "table" ("mki", "zxy", "abc") SELECT "test", "ops", NULL FROM "table2";',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 6)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], 'INSERT INTO "table" ("bar", "foo", "id") VALUES ("val", NULL, 1);')
        self.assertEqual(ordered_sql[3], 'INSERT INTO "table" ("abc", "mki", "zxy") SELECT NULL, "test", "ops" FROM "table2";')
        self.assertEqual(ordered_sql[4], sql[4])
        self.assertEqual(ordered_sql[5], sql[5])

    def test_long_insert(self):
        sql = [
            'BEGIN;',
            '--',
            'INSERT INTO "table" ("id", "field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8", "field9") VALUES (1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);',
            '--',
            'COMMIT;',
        ]

        ordered_sql = order_insert_statements(sql)

        self.assertEqual(len(ordered_sql), 5)
        self.assertEqual(ordered_sql[0], sql[0])
        self.assertEqual(ordered_sql[1], sql[1])
        self.assertEqual(ordered_sql[2], 'INSERT INTO "table" ("field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8", "field9", "id") VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);')
        self.assertEqual(ordered_sql[3], sql[3])
        self.assertEqual(ordered_sql[4], sql[4])
