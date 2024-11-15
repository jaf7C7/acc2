import pytest
from unittest.mock import MagicMock
from acc.app import Application


@pytest.fixture
def app():
    return Application(config_type=MagicMock(), ledger_type=MagicMock())


def test_get_date_returns_current_app_date(app):
    assert app.get_date() == {'date': app.date}


def test_set_date_sets_current_app_date(app):
    app.set_date('1999-12-31')
    assert app.get_date() == {'date': '1999-12-31'}


def test_exception_raised_if_new_date_is_not_a_valid_iso_format_date(app):
    with pytest.raises(ValueError):
        app.set_date('2000/01/01')


def test_get_ledger_returns_current_ledger_path(app):
    assert app.get_ledger() == {'ledger': app.ledger_path}


def test_set_ledger_sets_new_ledger_path(app):
    app.set_ledger('new_ledger')
    assert app.get_ledger() == {'ledger': 'new_ledger'}


def test_add_transactions_writes_new_transaction_to_ledger(app):
    transaction = {
        'type': 'debit',
        'amount': 1099,
        'description': 'Toilet paper (multipack).',
    }
    app.add_transaction(transaction)
    ledger = app.ledger_type(app.ledger_path)
    ledger.write.assert_called_with(
        [
            {
                'id': 0,
                'date': app.date,
                **transaction,
            }
        ],
        mode='a',
    )


def test_get_transactions_returns_list_of_recorded_transactions(app):
    ledger = app.ledger_type(app.ledger_path)
    attrs = {'read.side_effect': lambda: ['t1', 't2', '...', 'tN']}
    ledger.configure_mock(**attrs)
    assert app.get_transactions() == {'transactions': ['t1', 't2', '...', 'tN']}


def test_FileNotFoundError_gives_id_0(app):
    ledger = app.ledger_type(app.ledger_path)
    attrs = {'read.side_effect': FileNotFoundError}
    ledger.configure_mock(**attrs)
    transaction = {'type': 'debit', 'amount': 1099, 'description': 'Soup'}
    app.add_transaction(transaction)
    ledger.write.assert_called_with(
        [{'id': 0, 'date': app.date, **transaction}], mode='a'
    )
