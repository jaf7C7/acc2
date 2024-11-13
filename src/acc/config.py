class Config:
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        self.path = path
        self._date = '1970-01-01'

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date
        with open(self.path, mode='w') as f:
            f.write(new_date)
