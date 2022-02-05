import os
import tempfile

from Executor.file_manager import FileManager


def test_is_file():
    file = tempfile.TemporaryFile()
    assert FileManager.is_file(file.name) is True and os.path.exists(file.name) is True
    file.close()
    assert FileManager.is_file(file.name) is False and os.path.exists(file.name) is False


def test_is_directory():
    directory = tempfile.TemporaryDirectory()
    assert FileManager.is_directory(directory.name) is True and os.path.exists(directory.name) is True
    directory.cleanup()
    assert FileManager.is_directory(directory.name) is False and os.path.exists(directory.name) is False


def test_get_file_content():
    content = "HelloWorld"
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            tmp.write(content)
        assert FileManager.get_file_content(path) == content
    finally:
        os.remove(path)


def test_get_directory_content():
    directory = tempfile.TemporaryDirectory()
    file1 = tempfile.TemporaryFile(dir=directory.name)
    file2 = tempfile.TemporaryFile(dir=directory.name)
    result = FileManager.get_directory_content(directory.name)
    assert result == file1.name + '\n' + file2.name or result == file2.name + '\n' + file1.name
    directory.cleanup()
    assert FileManager


def test_get_current_directory():
    assert FileManager.get_current_directory() == os.getcwd()
