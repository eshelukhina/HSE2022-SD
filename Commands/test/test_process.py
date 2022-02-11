from Commands.process import Process
from Environment.impl import Environment
from Executor.context import Context


def test_print():
    process = Process(name='echo', args=["Hello World!"])
    context = Context(env_vars=Environment({}))
    process.execute(context)
    assert context.state
    assert context.state.get() == "Hello World!\n"
    assert not context.error


def test_env():
    process = Process(name='echo', args=["$x"])
    context = Context(env_vars=Environment({'x': 'Hello World!'}))
    process.execute(context)
    assert context.state
    assert context.state.get() == "Hello World!\n"
    assert not context.error


def test_process_with_error():
    process = Process(name='ca', args=[])
    context = Context(env_vars=Environment({}))
    process.execute(context)
    assert not context.state
    assert context.error
