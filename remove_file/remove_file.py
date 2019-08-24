import os

def delete_file(filename):
    os.remove(filename)

if __name__ == "__main__":
    delete_file('test_file.txt')
