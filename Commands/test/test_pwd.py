import os

from Commands.pwd import Pwd
from Executor.context import Context


def test_cur_dir():
    args = ['']
    result = os.getcwd() + '\n'
    pwd = Pwd(args=args)
    context = Context()
    output, ret_code = pwd.execute(context)
    assert ret_code == 0
    assert output == result
