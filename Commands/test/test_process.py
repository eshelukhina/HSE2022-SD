import sys

from Commands.process import Process
from Executor.context import Context


def test_print():
    process = Process(name=sys.executable, args=["-c", "print('test')"])
    context = Context(1)
    process.execute(context)
    assert context.state.is_present() is True
    assert context.state.get() == "test\n"
    assert context.error.is_empty() is True


def test_proces_with_error():
    process = Process(name=sys.executable, args=["-c", "prin('test')"])
    context = Context(1)
    process.execute(context)
    assert context.state.is_empty() is True
    assert context.error.is_present() is True
