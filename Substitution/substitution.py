from typing import Tuple

from Environment.impl import environment


class Substitution:
    """
    Substitution of variables in the input string and handling double and single quotes
    """

    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'
    DOLLAR = "$"
    env = environment

    def __init__(self):
        self.list_of_substitutions = []

    def __get_substitutions(self, s: str):
        i = 0
        while i < len(s):
            if s[i] == self.DOLLAR:
                a = i
                var, i = self.__extract_var(i, s)
                self.list_of_substitutions.append((var, (a, i - 1)))
            else:
                i += 1

    def __extract_var(self, i: int, s: str) -> Tuple[str, int]:
        var: str = s[i]
        i += 1
        while i < len(s) and s[i].isalpha():
            var += s[i]
            i += 1
        return var, i

    def __set_substitutions(self, s: str):
        diff = 0
        for elem in self.list_of_substitutions:
            var, positions = elem
            begin, end = positions

            var = var.replace(self.DOLLAR, '')
            new_value = self.env.get_value(name=var)

            a = s[:begin + diff]
            b = s[end + 1 + diff:]
            diff += len(new_value) - len(var) - 1
            s = a + new_value + b
        return s

    def __find_and_replace(self, s: str):
        self.__get_substitutions(s)
        s = self.__set_substitutions(s)
        self.list_of_substitutions.clear()
        return s

    def substitute(self, s: str) -> str:
        """
        Gets an input string
        Performs variable substitution and quotes
        :returns str - string with performed substitutions
        """

        i = 0
        result = ""
        while i < len(s):
            if s[i] == self.SINGLE_QUOTE:
                new_substr, new_i = self.__extract_quotes(self.SINGLE_QUOTE, i, s)
                i = new_i
                result += new_substr
            elif s[i] == self.DOUBLE_QUOTE:
                new_substr, new_i = self.__extract_quotes(self.DOUBLE_QUOTE, i, s)
                i = new_i
                result += new_substr
            elif s[i] == self.DOLLAR:
                substr = s[i]
                i += 1
                while i < len(s) and s[i].isalpha():
                    substr += s[i]
                    i += 1
                result += self.__find_and_replace(substr)
                i -= 1
            else:
                result += s[i]
            i += 1
        return result

    def __extract_quotes(self, quote: str, i: int, s: str):
        i_start = i
        i += 1
        while i < len(s) and s[i] != quote:
            i += 1
        if i >= len(s):
            if s[i - 1] == quote:
                sub_s = s[i_start:i]
                if quote == self.SINGLE_QUOTE:
                    res = sub_s
                else:
                    res = self.__find_and_replace(sub_s)
            else:
                raise IOError
            return res, i - 1
        elif s[i] == quote:
            sub_s = s[i_start:i + 1]
            if quote == self.SINGLE_QUOTE:
                res = sub_s
            else:
                res = self.__find_and_replace(sub_s)
        else:
            raise IOError
        return res, i
