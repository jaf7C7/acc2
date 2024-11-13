from unittest.mock import Mock
from acc.app import Application


def test_empty_date_param_returns_current_date():
    config = Mock()
    config.date = '1970-01-01'
    app = Application(config)
    assert app.run({'date': ''}) == {'date': '1970-01-01'}


def test_non_empty_date_param_sets_new_date():
    config = Mock()
    config.date = '1970-01-01'
    app = Application(config)
    app.run({'date': '1999-12-31'})
    assert app.config.date == '1999-12-31'


def test_empty_ledger_param_returns_current_ledger():
    config = Mock()
    config.ledger = 'my_ledger'
    app = Application(config)
    assert app.run({'ledger': ''}) == {'ledger': 'my_ledger'}
