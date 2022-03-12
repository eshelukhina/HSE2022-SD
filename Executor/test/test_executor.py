from Commands.echo import Echo
from Commands.exit import Exit
from Executor.executor import Executor


def test_no_commands():
    executor = Executor()
    executor.set_commands([])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output == ""


def test_one_command():
    args = ['hello world!']
    command = Echo(args=args)
    executor = Executor()
    executor.set_commands([command])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output == args[0] + '\n'


def test_exit():
    command = Exit(args=[])
    executor = Executor()
    executor.set_commands([command])
    output, ret_code = executor.run()
    assert ret_code == 0
    assert output == command.output
    assert executor.is_shell_terminated
