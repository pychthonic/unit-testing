"""This is a basic file with a function to test. The file
takes a filename and deletes it.
"""

import os

def delete_file(filename):
    """Deletes filename."""
    os.remove(filename)


if __name__ == "__main__":
    delete_file('test_file.txt')
