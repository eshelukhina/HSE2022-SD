from typing import List

from Executor.context import Context
from Executor.file_manager import FileManager


class Wc:
    def __init__(self, args: List[str]):
        self.args = args

    def execute(self, context: Context):
        """
        Проверяет, что все аргументы это пути до существующих файлов.
        Получает содержимое этих файлов и считает для каждого кол-во строк, слов и байтов.
        Записывает результат в Context
        """
        for arg in self.args:
            if not FileManager.is_file(arg):
                context.error = 'wc: No such file'
                return
        for arg in self.args:
            file_content = FileManager.get_file_content(arg)
            lines = file_content.count('\n')
            words = len([y for x in file_content.split('\n') for y in x.split(' ') if y != ''])
            num_bytes = len(file_content.encode())
            context.state += str(lines) + ' ' + str(words) + ' ' + str(num_bytes) + '\n'

    def __str__(self):
        return f'WC {self.args}'

    def __eq__(self, other):
        if isinstance(other, Wc):
            return self.args == other.args
        return False
