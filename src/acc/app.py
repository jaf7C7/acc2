from datetime import date
from acc.csvfile import CSVFile


class Application:
    """The central object which handles the main application logic."""

    def __init__(
        self, config_path='acc.conf', config_type=CSVFile, ledger_type=CSVFile
    ):
        self.config_path = config_path
        self.config_type = config_type
        self.ledger_path = 'ledger'
        self.ledger_type = ledger_type
        self._date = '1970-01-01'

    def get_date(self):
        return self._date

    def set_date(self, new_date):
        try:
            date.fromisoformat(new_date)
        except ValueError as e:
            raise e
        else:
            self._date = new_date

    def create_ledger(self):
        return self.ledger_type(self.ledger_path)

    def add_transaction(self, transaction):
        ledger = self.create_ledger()
        try:
            id = len(ledger.read())
        except FileNotFoundError:
            id = 0
        if transaction['type'] not in ('debit', 'credit'):
            raise ValueError
        try:
            int(transaction['amount'])
        except ValueError as e:
            raise e
        else:
            entry = [{'id': id, 'date': self.get_date(), **transaction}]
            ledger.write(entry, mode='a')

    def get_transactions(self):
        ledger = self.create_ledger()
        return ledger.read()
