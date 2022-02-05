class Context:
    def __init__(self, num_of_commands):
        self.num_of_commands = num_of_commands
        self.current_command = 1
        self.error = ''
        self.state = ''
