"""Test the integration of the Application and Config objects."""

import os
from acc.app import Application


def test_empty_date_param_returns_current_date():
    app = Application()
    assert app.run({'date': ''}) == {'date': '1970-01-01'}


def test_set_and_get_new_date():
    app = Application()
    app.run({'date': '2020-01-01'})
    assert app.run({'date': ''}) == {'date': '2020-01-01'}
    os.unlink(app.config.path)


def test_empty_ledger_param_returns_current_ledger():
    app = Application()
    assert app.run({'ledger': ''}) == {'ledger': 'ledger'}


def test_set_and_get_new_ledger():
    app = Application()
    app.run({'ledger': 'ledger'})
    assert app.run({'ledger': ''}) == {'ledger': 'ledger'}
    os.unlink(app.config.path)
