from unittest.mock import Mock
import pytest
from flask import g
from acc.api import api, get_app
from acc.app import Application


@pytest.fixture
def client():
    return api.test_client()


@pytest.fixture
def app():
    app = Mock(spec=Application)
    # Dummy values to allow JSON serialization.
    app.ledger_path = 'some_path'
    app.get_date.return_value = 'YYYY-MM-DD'
    app.get_transactions.return_value = [{'type': 'dummy transaction'}]
    with api.app_context():
        g.app = app
        yield g.app


def test_get_app():
    with api.app_context():
        app = get_app()
        assert app is get_app()


def test_get_date_endpoint(app, client):
    date = client.get('/date').get_json()['date']
    assert date == app.get_date()


def test_put_date_endpoint(app, client):
    client.put('/date', json={'date': '2020-01-01'})
    app.set_date.assert_called_with('2020-01-01')


def test_get_ledger_endpoint(app, client):
    ledger = client.get('/ledger').get_json()['ledger']
    assert ledger == app.ledger_path


def test_put_ledger_endpoint(app, client):
    client.put('/ledger', json={'ledger': 'new_ledger'})
    assert app.ledger_path == 'new_ledger'


def test_get_transaction_endpoint(app, client):
    transactions = client.get('/transactions').get_json()['transactions']
    assert transactions == app.get_transactions()


def test_post_transactions_endpoint(app, client):
    transaction = {'foo': 1, 'bar': 2}
    client.post('/transactions', json=transaction)
    app.add_transaction.assert_called_with(transaction)
