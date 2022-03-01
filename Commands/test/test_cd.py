import os

from Commands.cd import Cd
from Commands.ls import Ls
from Executor.context import Context
from Executor.executor import Executor


def test_cd_with_correct_arg():
    context = Context()
    cd = Cd(['../resources/one'])
    _, ret_code = cd.execute(context)
    ls = Ls([])
    output, _ = ls.execute(context)
    assert ret_code == 0
    assert output == '4.txt'


def test_cd_without_args():
    context = Context()
    cd = Cd(['../resources/two/three'])
    _, ret_code = cd.execute(context)
    ls = Ls([])
    output, _ = ls.execute(context)
    assert ret_code == 0
    assert output == '6.txt'
    cd = Cd([])
    _, ret_code = cd.execute(context)
    assert ret_code == 0
    assert Executor.current_directory == os.path.expanduser("~")


def test_cd_with_two_dots():
    context = Context()
    cd = Cd(['../resources/two/three'])
    _, ret_code = cd.execute(context)
    ls = Ls([])
    output, _ = ls.execute(context)
    assert ret_code == 0
    assert output == '6.txt'
    cd = Cd(['..'])
    _, ret_code = cd.execute(context)
    assert ret_code == 0
    output, _ = ls.execute(context)
    assert output == '5.txt\nthree'


def test_cd_with_many_args():
    context = Context()
    cd = Cd(['../resources', 'odd arg'])
    output, ret_code = cd.execute(context)
    assert ret_code == 1
    assert output == 'cd: too many arguments'


def test_cd_no_such_dir():
    context = Context()
    cd = Cd(['../resources/fifteen'])
    output, ret_code = cd.execute(context)
    assert ret_code == 2
    assert output.__contains__('cd: no such directory')
