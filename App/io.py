class IO:
    def __init__(self):
        pass

    @staticmethod
    def read(self):
        """
        Read user input
        :return: str
        """
        user_input = input(">>> ")
        return user_input

    @staticmethod
    def write(self, user_output, err_output):
        """
        Print command output
        :param user_output: successful command output
        :param err_output: failed command output
        """
        if err_output:
            print(f"{err_output.get()}")
        elif user_output:
            print(f"{user_output.get()}")
        else:
            print('', end='')
