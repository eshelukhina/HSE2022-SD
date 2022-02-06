from Commands.echo import Echo
from Commands.exit import Exit
from Executor.executor import Executor


def test_one_command():
    args = ['hello world!']
    command = Echo(args=args)
    executor = Executor()
    executor.set_commands([command])
    command_output, err_output = executor.run()
    assert command_output.get() == args[0]
    assert err_output.is_present() is False


def test_exit():
    command = Exit(args=[])
    executor = Executor()
    executor.set_commands([command])
    command_output, err_output = executor.run()
    assert command_output.get() is command.output
    assert err_output.is_present() is False
    assert executor.shell_terminated is True
