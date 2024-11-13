class Config:
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        self.path = path
        self._date = None
        self._ledger = None

    @property
    def date(self):
        try:
            with open(self.path) as f:
                self._date = f.read()
        except FileNotFoundError:
            self._date = '1970-01-01'
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date
        with open(self.path, mode='w') as f:
            f.write(new_date)

    @property
    def ledger(self):
        try:
            with open(self.path) as f:
                self._ledger = f.read()
        except FileNotFoundError:
            self._ledger = 'ledger'
        return self._ledger

    @ledger.setter
    def ledger(self, new_ledger):
        self._ledger = new_ledger
        with open(self.path, mode='w') as f:
            f.write(new_ledger)
