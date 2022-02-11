from Commands.echo import Echo
from Commands.exit import Exit
from Executor.executor import Executor


def test_no_commands():
    executor = Executor()
    executor.set_commands([])
    command_output, err_output = executor.run()
    assert not command_output
    assert not err_output


def test_one_command():
    args = ['hello world!']
    command = Echo(args=args)
    executor = Executor()
    executor.set_commands([command])
    command_output, err_output = executor.run()
    assert command_output.get() == args[0] + '\n'
    assert not err_output


def test_exit():
    command = Exit(args=[])
    executor = Executor()
    executor.set_commands([command])
    command_output, err_output = executor.run()
    assert command_output.get() == command.output
    assert executor.shell_terminated
    assert not err_output
