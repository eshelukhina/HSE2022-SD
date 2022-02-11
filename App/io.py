class IO:
    def __init__(self):
        pass

    @staticmethod
    def read():
        """
        Read user input
        :rtype str
        """
        user_input = input(">>> ")
        return user_input

    @staticmethod
    def write(output: str):
        """
        Print output
        :param output
        """
        print(output)
