import filemanager
import os

def test_copy_file_or_directory():
    filemanager.copy_file_or_directory('filemanager.py', 'filemanager1.py')
    assert 'filemanager1.py' in os.listdir()


def test_filenames():
    assert 'filemanager.py' in filemanager.filenames()


def test_author_info():
    assert filemanager.author_info() == 'Leonid Orlov'

