import pytest
from unittest.mock import Mock
from acc.app import Application


@pytest.fixture
def app():
    return Application(Mock())


def test_empty_date_param_returns_current_date(app):
    app.config.date = '1970-01-01'
    assert app.run({'date': ''}) == {'date': '1970-01-01'}


def test_non_empty_date_param_sets_new_date(app):
    app.config.date = '1970-01-01'
    app.run({'date': '1999-12-31'})
    assert app.config.date == '1999-12-31'


def test_empty_ledger_param_returns_current_ledger(app):
    app.config.ledger = 'my_ledger'
    assert app.run({'ledger': ''}) == {'ledger': 'my_ledger'}


def test_non_empty_ledger_param_sets_new_ledger(app):
    app.config.ledger = 'old_ledger'
    app.run({'ledger': 'new_ledger'})
    assert app.config.ledger == 'new_ledger'
