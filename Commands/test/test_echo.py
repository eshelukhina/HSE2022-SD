from Commands.echo import Echo
from Executor.context import Context


def test_one_arg():
    args = ["hello world !"]
    result = "hello world !"
    echo = Echo(args=args)
    context = Context(1)
    echo.execute(context)
    assert context.state.is_present() is True
    assert context.state.get() == result
    assert context.error.is_empty() is True


def test_several_args():
    args = ["hello", "world", "!"]
    result = "hello world !"
    echo = Echo(args=args)
    context = Context(1)
    echo.execute(context)
    assert context.state.is_present() is True
    assert context.state.get() == result
    assert context.error.is_empty() is True
