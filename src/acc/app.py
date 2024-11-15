from datetime import date
from acc.models import CSVFile


class Application:
    """The central object which handles the main application logic."""

    def __init__(
        self, config_path='acc.conf', config_type=CSVFile, ledger_type=CSVFile
    ):
        self.config_path = config_path
        self.config_type = config_type
        self.ledger_path = 'ledger'
        self.ledger_type = ledger_type
        self.date = '1970-01-01'

    def run(self, args):
        """Runs the application with the given arguments."""
        if 'date' in args:
            if args['date'] != '':
                try:
                    date.fromisoformat(args['date'])
                except ValueError as e:
                    raise (e)
                self.date = args['date']
            return {'date': self.date}

        elif 'ledger' in args:
            if args['ledger'] != '':
                self.ledger_path = args['ledger']
            return {'ledger': self.ledger_path}

        elif 'transaction' in args:
            ledger = self.ledger_type(self.ledger_path)
            try:
                id = len(ledger.read())
            except FileNotFoundError:
                id = 0
            transaction = {
                'id': id,
                'date': self.date,
                **args['transaction'],
            }
            ledger.write([transaction], mode='a')

        elif 'report' in args:
            ledger = self.ledger_type(self.ledger_path)
            return {'transactions': ledger.read()}
