import os

from Commands.ls import Ls
from Executor.context import Context
from Executor.executor import Executor


def test_ls_without_args():
    context = Context()
    Executor.current_directory = os.getcwd()
    Executor.current_directory = '../resources'
    ls = Ls([])
    output, ret_code = ls.execute(context)
    actual_output_list = output.split('\n')
    expected_output_list = ['two', 'one', '1.txt', '2.txt', '3.txt']

    assert ret_code == 0
    assert len(expected_output_list) == len(actual_output_list)
    for file in actual_output_list:
        assert expected_output_list.__contains__(file)


def test_ls_with_correct_arg():
    context = Context()
    Executor.current_directory = os.getcwd()
    ls = Ls(['../resources'])
    output, ret_code = ls.execute(context)
    actual_output_list = output.split('\n')
    expected_output_list = ['two', 'one', '1.txt', '2.txt', '3.txt']

    assert ret_code == 0
    assert len(expected_output_list) == len(actual_output_list)
    for file in actual_output_list:
        assert expected_output_list.__contains__(file)


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
