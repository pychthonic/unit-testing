"""This is a basic file with a function to test. The file
takes a filename and deletes it.
"""

import os

def delete_file(filename):
    """Deletes filename."""
    os.remove(filename)


if __name__ == "__main__":
    if os.path.exists('test_file.txt'):
        delete_file('test_file.txt')
        print('test_file.txt found and deleted.')
    else:
        print('test_file.txt not found.')
