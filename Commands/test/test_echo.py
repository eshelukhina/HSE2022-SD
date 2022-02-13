from Commands.echo import Echo
from Executor.context import Context


def test_one_arg():
    args = ["hello world !"]
    result = "hello world !"
    echo = Echo(args=args)
    context = Context()
    ret_code = echo.execute(context)
    assert context.state.get() == result
    assert ret_code == 0


def test_several_args():
    args = ["hello", "world", "!"]
    echo = Echo(args=args)
    context = Context()
    ret_code = echo.execute(context)
    assert ret_code == 0
    assert context.state.get() == "hello world !"
