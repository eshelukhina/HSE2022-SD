from optional import Optional


class Context:
    def __init__(self, *, env_vars):
        self.error = Optional.empty()
        self.state = Optional.empty()
        self.env = env_vars
