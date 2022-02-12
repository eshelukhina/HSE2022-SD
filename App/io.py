from optional import Optional


class IO:
    """
    Component responsible for communication with the outside world.
    """

    def __init__(self):
        pass

    @staticmethod
    def read():
        """
        Read user input
        :rtype str
        """
        return input(">>> ")

    @staticmethod
    def write(output: Optional):
        """
        Print output
        :param output
        """
        print(output.get(), end='\n')
