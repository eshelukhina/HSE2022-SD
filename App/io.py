class IO:
    def __init__(self):
        pass

    def read(self):
        """
        Read user input
        :return: str
        """
        user_input = input(">>>")
        return user_input

    def write(self, user_output, err_output):
        """
        Print command output
        :param user_output: successful command output
        :param err_output: failed command output
        """
        if err_output.is_present() is True:
            print(user_output.get())
        else:
            print(f"Error: {err_output.get()}")
