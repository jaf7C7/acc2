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


def test_get_app_returns_same_object_each_time():
    with api.app_context():
        app = get_app()
        assert app is get_app()


def test_get_date_endpoint_returns_the_date(app, client):
    date = client.get('/date').get_json()['date']
    assert date == app.get_date()


def test_put_date_endpoint_sets_new_date(app, client):
    client.put('/date', data={'date': '2020-01-01'})
    app.set_date.assert_called_with('2020-01-01')


def test_get_ledger_endpoint_returns_the_ledger_path(app, client):
    ledger = client.get('/ledger').get_json()['ledger']
    assert ledger == app.ledger_path


def test_put_ledger_endpoint_sets_new_ledger_path(app, client):
    client.put('/ledger', data={'ledger': 'new_ledger'})
    assert app.ledger_path == 'new_ledger'


def test_get_transaction_endpoint_returns_list_of_transactions(app, client):
    transactions = client.get('/transactions').get_json()['transactions']
    assert transactions == app.get_transactions()


def test_post_transactions_endpoint_adds_new_transaction(app, client):
    transaction = {'foo': '1', 'bar': '2'}  # HTTP form data is a string.
    client.post('/transactions', data=transaction)
    app.add_transaction.assert_called_with(transaction)
