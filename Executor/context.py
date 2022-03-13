from optional import Optional


from Environment.impl import environment


class Context:
    """
    Stores the execution context of the commands.
    """

    def __init__(self):
        self.state = Optional.empty()
        self.env = environment
