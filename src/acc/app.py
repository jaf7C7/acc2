from datetime import date
from acc.config import Config


class Application:
    """The central object which runs the application logic with the given arguments."""

    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def run(self, args):
        if 'date' in args:
            if args['date'] != '':
                try:
                    date.fromisoformat(args['date'])
                except ValueError as e:
                    raise (e)
                self.config.date = args['date']
            return {'date': self.config.date}
        elif 'ledger' in args:
            if args['ledger'] != '':
                self.config.ledger = args['ledger']
            return {'ledger': self.config.ledger}
