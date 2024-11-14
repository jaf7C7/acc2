"""Test the integration of the Application, Config and Ledger objects."""

import os
import pytest
from acc.app import Application


@pytest.fixture
def app(tmp_path):
    config_path = os.path.join(tmp_path, 'test_config')
    ledger_path = os.path.join(tmp_path, 'test_ledger')
    app = Application()
    app.config.path = config_path
    app.ledger.path = ledger_path
    yield app
    for f in config_path, ledger_path:
        try:
            os.unlink(f)
        except FileNotFoundError:
            pass


def test_empty_date_param_returns_current_date(app):
    assert app.run({'date': ''}) == {'date': '1970-01-01'}


def test_set_and_get_new_date(app):
    app.run({'date': '2020-01-01'})
    assert app.run({'date': ''}) == {'date': '2020-01-01'}


def test_empty_ledger_param_returns_current_ledger(app):
    assert app.run({'ledger': ''}) == {'ledger': 'ledger'}


def test_set_and_get_new_ledger(app):
    app.run({'ledger': 'ledger'})
    assert app.run({'ledger': ''}) == {'ledger': 'ledger'}


def test_add_and_report_transactions(app):
    app.run(
        {
            'transaction': {
                'type': 'credit',
                'amount': 1099,
                'description': 'Gift from Grandma.',
            }
        }
    )
    assert app.run({'report': ''}) == {
        'transactions': [
            {
                'id': '0',
                'date': str(app.config.date),
                'type': 'credit',
                'amount': '1099',
                'description': 'Gift from Grandma.',
            }
        ]
    }
