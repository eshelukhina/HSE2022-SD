from typing import List

from optional.optional import Optional

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
                context.error = Optional.of(f'wc: {arg}: No such file')
                return
        final_result = []
        for arg in self.args:
            result = []
            file_content = FileManager.get_file_content(arg)

            # Считаем количество строк, как количество знаков перевода строки
            lines = file_content.count('\n')
            result.append(str(lines))

            # Разбиваем содержимое файла на строки, потом разбиваем строки по пробелам и удаляем пустые строки
            words = len([y for x in file_content.split('\n') for y in x.split(' ') if y != ''])
            result.append(str(words))

            # Переводим содержимое файла в байты и считаем их количество
            num_bytes = len(file_content.encode())
            result.append(str(num_bytes))

            result.append(arg)
            final_result.append(' '.join(result))
        context.state = Optional.of('\n'.join(final_result))

    def __str__(self):
        return f'WC {self.args}'

    def __eq__(self, other):
        if isinstance(other, Wc):
            return self.args == other.args
        return False
