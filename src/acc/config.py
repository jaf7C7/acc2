import csv


class Config:
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        self.path = path
        self._date = None
        self._ledger = None

    @property
    def date(self):
        config = self.read()
        self._date = config.get('date', '1970-01-01')
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date
        self.write([{'date': self._date, 'ledger': self._ledger}])

    @property
    def ledger(self):
        config = self.read()
        self._ledger = config.get('ledger', 'ledger')
        return self._ledger

    @ledger.setter
    def ledger(self, new_ledger):
        self._ledger = new_ledger
        self.write([{'date': self._date, 'ledger': self._ledger}])

    def read(self):
        try:
            with open(self.path, newline='') as f:
                config = next(csv.DictReader(f))
        except FileNotFoundError:
            config = {}
        return config

    def write(self, lines):
        with open(self.path, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=lines[0].keys())
            writer.writeheader()
            for line in lines:
                writer.writerow(line)
