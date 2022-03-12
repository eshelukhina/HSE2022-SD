from Commands.cat import Cat
from Commands.echo import Echo
from Commands.exit import Exit
from Commands.pwd import Pwd
from Executor.executor import Executor


def test_no_commands():
    executor = Executor()
    executor.set_commands([])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert not output


def test_one_command():
    args = ['hello world!']
    command = Echo(args=args)
    executor = Executor()
    executor.set_commands([command])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output.get() == args[0]


def test_exit():
    command = Exit(args=[])
    executor = Executor()
    executor.set_commands([command])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output.get() == command.output
    assert executor.is_shell_terminated


def test_several_commands():
    result = 'hello world !'
    command1 = Echo(args=['hello', 'world', '!'])
    command2 = Cat(args=[])
    executor = Executor()
    executor.set_commands([command1, command2])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output.get() == result


def test_several_commands_exit():
    result = ''
    command1 = Echo(args=['hello', 'world', '!'])
    command2 = Exit(args=[])
    command3 = Cat(args=[])
    executor = Executor()
    executor.set_commands([command1, command2, command3])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output.get() == result
    assert executor.is_shell_terminated


def test_pipe_err_output():
    result = 'pwd: too many arguments'
    command1 = Echo(args=['hello', 'world', '!'])
    command2 = Pwd(args=[])
    command3 = Cat(args=[])
    executor = Executor()
    executor.set_commands([command1, command2, command3])
    output, ret_code = executor.run()
    assert ret_code == 1
    assert output.get() == result
