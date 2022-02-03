import os

from Executor.file_manager import FileManager
from Executor.path_types import PathTypes


def test_get_file_type_file():
    file = "directory/test1.txt"
    file_manager = FileManager(file)
    assert file_manager.get_file_type() == PathTypes.file


def test_get_file_type_directory():
    file = "directory"
    file_manager = FileManager(file)
    assert file_manager.get_file_type() == PathTypes.directory


def test_get_file_content_file():
    file = "directory/test1.txt"
    content = "HelloWorld"
    file_manager = FileManager(file)
    file_manager.get_file_type()
    assert file_manager.get_file_content() == content


def test_get_file_content_directory():
    file = "directory"
    content = "test1.txt\ntest2.txt\n"
    file_manager = FileManager(file)
    file_manager.get_file_type()
    assert file_manager.get_file_content() == content


def test_get_current_directory():
    assert FileManager.get_current_directory() == os.getcwd()


if __name__ == '__main__':
    test_get_file_type_file()
    test_get_file_type_directory()
    test_get_file_content_file()
    test_get_file_content_directory()
    test_get_current_directory()
