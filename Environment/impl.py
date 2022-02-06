import copy
from typing import NoReturn


# Класс, ответственный за поддержание переменных окружения
class Environment:
    def __init__(self):
        self.vars = {}

    def add_var(self, *, name, value) -> NoReturn:
        """
        Update environment variable
        :param name - var name
        :param value - new value
        """
        self.vars[name] = value

    def get_value(self, *, name) -> str:
        """
        Get environment variable.
        Return empty line if there is no such var
        :returns str
        """
        return self.vars.get(name, '')

    def get_vars(self):
        """
        Returns copy of variables dictionary
        :returns Dict[str, str]
        """
        return copy.deepcopy(self.vars)
