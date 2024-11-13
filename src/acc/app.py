from datetime import date
from acc.config import Config


class Application:
    """The central object which handles the main application logic."""

    def __init__(self, config=None, ledger_type=None):
        if config is None:
            config = Config()
        self.config = config
        self.ledger = ledger_type(self.config.ledger)

    def run(self, args):
        """Runs the application with the given arguments."""
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

        elif 'transaction' in args:
            self.ledger.append(args['transaction'])
