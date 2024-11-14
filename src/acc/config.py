from acc.models import CSVFile


class Config(CSVFile):
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        super().__init__(path)
        self._date = None
        self._ledger = None

    @property
    def date(self):
        try:
            self._date = self.read().pop(0).get('date')
        except FileNotFoundError:
            self._date = '1970-01-01'
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date
        self.write([{'date': self._date, 'ledger': self._ledger}])

    @property
    def ledger(self):
        try:
            self._ledger = self.read().pop(0).get('ledger')
        except FileNotFoundError:
            self._ledger = 'ledger'
        return self._ledger

    @ledger.setter
    def ledger(self, new_ledger):
        self._ledger = new_ledger
        self.write([{'date': self._date, 'ledger': self._ledger}])
