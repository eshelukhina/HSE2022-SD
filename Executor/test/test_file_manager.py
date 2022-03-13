import collections
import os
import tempfile

from Executor.file_manager import FileManager


def test_is_file():
    file = tempfile.TemporaryFile()
    assert FileManager.is_file(file.name) is True and os.path.exists(file.name) is True
    file.close()
    assert FileManager.is_file(file.name) is False and os.path.exists(file.name) is False


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
    with tempfile.TemporaryDirectory() as directory:
        file1 = open(os.path.join(directory, "file1.txt"), "w+")
        file1.close()
        file2 = open(os.path.join(directory, "file2.xt"), "w+")
        file2.close()
        result = FileManager.get_directory_content(directory)
        assert collections.Counter(result) == collections.Counter([file1.name, file2.name])


def test_get_current_directory():
    assert FileManager.get_current_directory() == os.getcwd()
