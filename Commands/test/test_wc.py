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
        assert context.state == '0 0 0\n'
    finally:
        os.remove(path)


def test_not_empty_file():
    content = ' '
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state == '0 0 1\n'
    finally:
        os.remove(path)


def test_empty_last_line():
    content = 'hello\n'
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state == '1 1 6\n'
    finally:
        os.remove(path)


def test_not_empty_last_line():
    content = 'hello\nworld'
    context = Context(1)
    fd, path = create_tmp_file(content)
    try:
        wc = Wc([path])
        wc.execute(context)
        assert context.state == '1 2 11\n'
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
        assert context.state == '1 2 11\n1 2 11\n'
    finally:
        os.remove(path1)
        os.remove(path2)
