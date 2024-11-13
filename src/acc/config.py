class Config:
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        self.path = path
        self.date = '1970-01-01'
        self.ledger = 'ledger'
