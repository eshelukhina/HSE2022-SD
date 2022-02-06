import os
import tempfile

from Commands.wc import Wc
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
        wc = Wc([path])
        wc.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == '0 0 0 {}'.format(path)
    finally:
        os.remove(path)


def test_not_empty_file():
    content = ' '
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == '0 0 1 {}'.format(path)
    finally:
        os.remove(path)


def test_with_error():
    error = 'wc: f: No such file'
    context = Context(1)
    wc = Wc(['f'])
    wc.execute(context)
    assert context.error.is_present() is True
    assert context.error.get() == error


def test_empty_last_line():
    content = 'hello\n'
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == '1 1 6 {}'.format(path)
    finally:
        os.remove(path)


def test_not_empty_last_line():
    content = 'hello\nworld'
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == '1 2 11 {}'.format(path)
    finally:
        os.remove(path)


def test_with_files():
    content = 'hello\nworld'
    context = Context(1)
    fd1, path1 = create_tmp_file(content)
    fd2, path2 = create_tmp_file(content)
    try:
        wc = Wc([path1, path2])
        wc.execute(context)
        assert context.state.is_present() is True
        assert context.state.get() == '1 2 11 {0}\n1 2 11 {1}'.format(path1, path2)
    finally:
        os.remove(path1)
        os.remove(path2)
