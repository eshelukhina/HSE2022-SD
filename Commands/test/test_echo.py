from Commands.echo import Echo
from Executor.context import Context


def test_one_arg():
    args = ["hello world !"]
    result = "hello world !\n"
    echo = Echo(args=args)
    context = Context()
    output, ret_code = echo.execute(context)
    assert output == result
    assert ret_code == 0


def test_several_args():
    args = ["hello", "world", "!"]
    echo = Echo(args=args)
    context = Context()
    output, ret_code = echo.execute(context)
    assert ret_code == 0
    assert output == "hello world !\n"
