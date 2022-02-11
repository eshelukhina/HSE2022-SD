import os
import tempfile

from Commands.wc import Wc
from Executor.context import Context


def create_tmp_file(content):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return fd, path


def create_file_and_run_test(content, lines, words, num_bytes):
    context = Context(env_vars={})
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'{lines} {words} {num_bytes} {path}\n'
    finally:
        os.remove(path)


def test_empty_file():
    content = ''
    lines, words, num_bytes = 0, 0, 0
    create_file_and_run_test(content, lines, words, num_bytes)


def test_not_empty_file():
    content = ' '
    lines, words, num_bytes = 0, 0, 1
    create_file_and_run_test(content, lines, words, num_bytes)


def test_with_error():
    error = 'wc: no such file f'
    context = Context(env_vars={})
    wc = Wc(['f'])
    wc.execute(context)
    assert context.error
    assert context.error.get() == error


def test_empty_last_line():
    content = 'hello\n'
    lines, words, num_bytes = 1, 1, 6
    create_file_and_run_test(content, lines, words, num_bytes)


def test_not_empty_last_line():
    content = 'hello\nworld'
    lines, words, num_bytes = 1, 2, 11
    create_file_and_run_test(content, lines, words, num_bytes)


def test_with_files():
    content = 'hello\nworld'
    context = Context(env_vars={})
    fd1, path1 = create_tmp_file(content)
    fd2, path2 = create_tmp_file(content)
    try:
        wc = Wc([path1, path2])
        wc.execute(context)
        assert context.state
        assert context.state.get() == f'1 2 11 {path1}\n1 2 11 {path2}\n'
    finally:
        os.remove(path1)
        os.remove(path2)
