import os
import tempfile

from Commands.cat import Cat
from Executor.context import Context


def create_tmp_file(content):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return fd, path


def test_empty_file():
    content = ''
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        cat = Cat([path])
        cat.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == content
    finally:
        os.remove(path)


def test_not_empty_file():
    content = 'helloworld\n'
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        cat = Cat([path])
        cat.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == content
    finally:
        os.remove(path)


def test_with_error():
    error = 'cat: f: No such file'
    context = Context(1)
    cat = Cat(['f'])
    cat.execute(context)
    assert context.state.is_empty() is True
    assert context.error.is_present() is True
    assert context.error.get() == error


def test_with_files():
    content = 'helloworld\n'
    context = Context(1)
    fd1, path1 = create_tmp_file(content)
    fd2, path2 = create_tmp_file(content)
    try:
        cat = Cat([path1, path2])
        cat.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == 'helloworld\nhelloworld\n'
    finally:
        os.remove(path1)
        os.remove(path2)
