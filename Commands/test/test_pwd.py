import os
from Commands.pwd import Pwd
from Executor.context import Context


def test_cur_dir():
    args = ['']
    result = os.getcwd()
    echo = Pwd(args=args)
    context = Context(1)
    echo.execute(context)
    assert context.state.get() == result
    assert context.error.is_empty() is True
