import sys

from Commands.process import Process
from Executor.context import Context


def test_print():
    process = Process(name=sys.executable, args=["-c", "print('test')"])
    context = Context(1)
    process.execute(context)
    assert context.state == "test\n"
    assert context.error == ''


def test_proces_with_error():
    process = Process(name=sys.executable, args=["-c", "prin('test')"])
    context = Context(1)
    process.execute(context)
    assert context.state == ''
    assert context.error != ''
