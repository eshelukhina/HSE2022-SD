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
    context = Context(env_vars={})
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'0 0 0 {path}'
    finally:
        os.remove(path)


def test_not_empty_file():
    content = ' '
    context = Context(env_vars={})
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'0 0 1 {path}'
    finally:
        os.remove(path)


def test_with_error():
    error = 'wc: no such file f'
    context = Context(env_vars={})
    wc = Wc(['f'])
    wc.execute(context)
    assert context.error
    assert context.error.get() == error


def test_empty_last_line():
    content = 'hello\n'
    context = Context(env_vars={})
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'1 1 6 {path}'
    finally:
        os.remove(path)


def test_not_empty_last_line():
    content = 'hello\nworld'
    context = Context(env_vars={})
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'1 2 11 {path}'
    finally:
        os.remove(path)


def test_with_files():
    content = 'hello\nworld'
    context = Context(env_vars={})
    fd1, path1 = create_tmp_file(content)
    fd2, path2 = create_tmp_file(content)
    try:
        wc = Wc([path1, path2])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'1 2 11 {path1}\n1 2 11 {path2}'
    finally:
        os.remove(path1)
        os.remove(path2)
