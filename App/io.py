import sys


class IO:
    def __init__(self):
        pass

    @staticmethod
    def read():
        """
        Read user input and return him.
        Print empty line and return None if a signal SIGINT was sent.
        Print empty line and exit if an empty line was entered
        :rtype str
        """
        try:
            return input(">>> ")
        except KeyboardInterrupt:
            print('')
            return None
        except EOFError:
            print('')
            sys.exit(0)

    @staticmethod
    def write(output: str):
        """
        Print output
        :param output
        """
        print(output, end='')
