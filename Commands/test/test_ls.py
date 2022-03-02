from Commands.ls import Ls
from Executor.context import Context


def test_ls_without_args():
    context = Context()
    ls = Ls([])
    output, ret_code = ls.execute(context)
    assert ret_code == 0
    assert output == 'test_ls.py\ntest_process.py\n__init__.py\ntest_pwd.py' \
                     '\ntest_wc.py\ntest_echo.py\ntest_cat.py\ntest_grep.py'


def test_ls_with_correct_arg():
    context = Context()
    ls = Ls(['../resources'])
    output, ret_code = ls.execute(context)
    assert ret_code == 0
    assert output == 'two\none\n1.txt\nfour\n2.txt\n3.txt'


def test_ls_with_many_args():
    context = Context()
    ls = Ls(['../resources', 'odd arg'])
    output, ret_code = ls.execute(context)
    assert ret_code == 1
    assert output == 'ls: too many arguments'


def test_ls_no_such_dir():
    context = Context()
    ls = Ls(['../resources/fifteen'])
    output, ret_code = ls.execute(context)
    assert ret_code == 2
    assert output.__contains__('ls: no such directory')

if __name__ == '__main__':
    print("aa")