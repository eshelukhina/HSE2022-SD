from optional import Optional

from Environment.impl import Environment


class Context:
    def __init__(self, *, env_vars: Environment):
        """
        Сlass that stores the execution context of the commands.
        :param error: command execution error message
        :param state: result of the previous command
        :param env_vars: enviroment
        """
        self.error = Optional.empty()
        self.state = Optional.empty()
        self.env = env_vars
