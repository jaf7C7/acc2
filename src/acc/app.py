from acc.config import Config


class Application:
    """The central object which runs the application logic with the given arguments."""
    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def run(self, args):
        return {'date': self.config.date}
