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
    context = Context()
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        ret_code = wc.execute(context)
        assert ret_code == 0
        assert context.state.get() == f'{lines} {words} {num_bytes} {path}'
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
    context = Context()
    wc = Wc(['f'])
    ret_code = wc.execute(context)
    assert ret_code != 0
    assert context.state.get() == error


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
    context = Context()
    fd1, path1 = create_tmp_file(content)
    fd2, path2 = create_tmp_file(content)
    try:
        wc = Wc([path1, path2])
        ret_code = wc.execute(context)
        assert ret_code == 0
        assert context.state.get() == f'1 2 11 {path1}\n1 2 11 {path2}'
    finally:
        os.remove(path1)
        os.remove(path2)
