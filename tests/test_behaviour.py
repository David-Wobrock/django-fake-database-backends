import unittest
import subprocess
from tests.testcases import FakeBackendsTestCase


class BehaviourTest(FakeBackendsTestCase):
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
