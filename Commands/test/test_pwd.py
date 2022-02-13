import os

from Commands.pwd import Pwd
from Executor.context import Context


def test_cur_dir():
    args = []
    result = os.getcwd()
    pwd = Pwd(args=args)
    context = Context()
    ret_code = pwd.execute(context)
    assert ret_code == 0
    assert context.state.get() == result


def test_non_empty_dir():
    args = ['hello world!']
    err_result = "pwd: too many arguments"
    pwd = Pwd(args=args)
    context = Context()
    ret_code = pwd.execute(context)
    assert ret_code == 1
    assert context.state.get() == err_result
