import unittest
import os
import remove_file
import tempfile


class TestRemove(unittest.TestCase):
    def setUp(self):
        with open('test_file', 'w') as f:
            f.write('this is a test')

    def test_remove(self):
        self.assertTrue(os.path.exists('test_file'))
        remove_file.delete_file('test_file')
        self.assertFalse(os.path.exists('test_file'))


if __name__ == "__main__":
    unittest.main()
