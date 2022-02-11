from Commands.echo import Echo
from Executor.context import Context


def test_one_arg():
    args = ["hello world !"]
    result = "hello world !\n"
    echo = Echo(args=args)
    context = Context(env_vars={})
    echo.execute(context)
    assert context.state.get() == result
    assert not context.error


def test_several_args():
    args = ["hello", "world", "!"]
    result = "hello world !\n"
    echo = Echo(args=args)
    context = Context(env_vars={})
    echo.execute(context)
    assert context.state.get() == result
    assert not context.error
