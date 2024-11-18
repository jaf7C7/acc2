import os
import pytest
from acc.app import Application


@pytest.fixture
def app(tmp_path):
    os.chdir(tmp_path)
    app = Application()
    yield app
    for f in app.config_path, app.ledger_path:
        try:
            os.unlink(f)
        except FileNotFoundError:
            pass


def test_set_and_get_new_date(app):
    app.set_date('2020-01-01')
    assert app.get_date() == '2020-01-01'


def test_set_and_get_new_ledger(app):
    app.ledger_path = 'ledger'
    assert app.ledger_path == 'ledger'


def test_add_and_get_transaction(app):
    transaction = {
        'type': 'credit',
        'amount': '1099',
        'description': 'Gift from Grandma.',
    }
    app.add_transaction(transaction)
    assert app.get_transactions() == [
        {
            'id': '0',
            'date': str(app.get_date()),
            **transaction,
        }
    ]
