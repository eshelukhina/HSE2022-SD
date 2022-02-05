class IO:
    def __init__(self):
        pass

    def read(self):
        user_input = input(">>>")
        return user_input

    def write(self, user_output, err_output):
        if err_output is None:
            print(user_output)
        else:
            print(f"Error: {err_output}")
