from unittest.mock import MagicMock
import pytest
from flask import g
from acc.api import api, get_app


@pytest.fixture
def client():
    return api.test_client()


@pytest.fixture
def app():
    with api.app_context():
        g.app = MagicMock()
        yield g.app


def test_get_app():
    with api.app_context():
        app = get_app()
        assert app is get_app()


def test_get_date_endpoint(app, client):
    client.get('/date')
    app.get_date.assert_called()


def test_put_date_endpoint(app, client):
    client.put('/date', json={'date': '2020-01-01'})
    app.set_date.assert_called_with('2020-01-01')


def test_get_ledger_endpoint(app, client):
    client.get('/ledger')
    app.get_ledger.assert_called()


def test_put_ledger_endpoint(app, client):
    client.put('/ledger', json={'ledger': 'new_ledger'})
    app.set_ledger.assert_called_with('new_ledger')


def test_get_transaction_endpoint(app, client):
    client.get('/transactions')
    app.get_transactions.assert_called()


def test_post_transactions_endpoint(app, client):
    transaction = {'type': 'debit', 'amount': 1099, 'description': 'Maltesers'}
    client.post('/transactions', json=transaction)
    app.add_transaction.assert_called_with(transaction)
