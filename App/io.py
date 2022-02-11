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
    def write(output: str):
        """
        Print output
        :param output
        """
        print(output, end='')
