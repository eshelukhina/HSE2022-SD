import io


class Context:
    def __init__(self, num_of_commands):
        self.num_of_commands = num_of_commands
        self.current_command = 1
        self.error = io.BytesIO(b'')
        self.state = io.BytesIO(b'')
