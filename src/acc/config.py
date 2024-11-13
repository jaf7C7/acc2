class Config:
    """Represents the persistent state of the application."""

    def __init__(self, path='.acc.conf'):
        self.path = path

    def get_date(self):
        return '1970-01-01'
