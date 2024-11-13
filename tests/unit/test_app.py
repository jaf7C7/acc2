from unittest.mock import Mock
from acc.app import Application


def test_empty_date_param_returns_default_date():
    config = Mock()
    config.date = '1970-01-01'
    app = Application(config)
    assert app.run({'date': ''}) == {'date': '1970-01-01'}
