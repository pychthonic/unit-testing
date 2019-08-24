"""This is a unit test script to test remove_file.py
It creates a file called test_file, tests that it exists,
then deletes it, and tests that it has been deleted."""

import os
import unittest

import remove_file


class TestRemove(unittest.TestCase):
    """The setUp method creates test_file and writes
    a string to it. The test_remove method tests that
    the file exists, removes it, then tests that it's
    gone.
    """

    def setUp(self):
        with open('test_file', 'w') as file_descriptor:
            file_descriptor.write('this is a test')

    def test_remove(self):
        """Tests that file exists, deletes file, tests
        that file has been deleted.
        """
        self.assertTrue(os.path.exists('test_file'))
        remove_file.delete_file('test_file')
        self.assertFalse(os.path.exists('test_file'))


if __name__ == "__main__":
    unittest.main()
