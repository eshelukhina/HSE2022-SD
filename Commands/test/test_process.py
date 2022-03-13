import os

from Commands.process import Process
from Environment.impl import Environment
from Executor.context import Context


def test_print():
    process = Process(name='echo', args=["Hello World!"])
    context = Context()
    output, ret_code = process.execute(context)
    assert ret_code == 0
    assert output == "Hello World!\n"


def test_env():
    if os.name == 'nt':
        return
    process = Process(name='echo', args=["$x"])
    context = Context(env=Environment({'x': 'Hello World!'}))
    output, ret_code = process.execute(context)
    assert output == "Hello World!\n"
    assert ret_code == 0


def test_process_with_error():
    process = Process(name='ca', args=[])
    context = Context(env=Environment({}))
    output, ret_code = process.execute(context)
    assert ret_code != 0
