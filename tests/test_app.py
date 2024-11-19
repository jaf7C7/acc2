import pytest
from unittest.mock import MagicMock
from acc.app import Application


@pytest.fixture
def app():
    return Application(config_type=MagicMock(), ledger_type=MagicMock())


def test_set_date_sets_current_app_date(app):
    new_date = '1999-12-31'
    app.set_date(new_date)
    assert app.get_date() == new_date


def test_value_error_raised_if_new_date_is_not_a_valid_iso_format_date(app):
    with pytest.raises(ValueError):
        app.set_date('2000/01/01')


def test_create_ledger(app):
    app.create_ledger()
    app.ledger_type.assert_called_with(app.ledger_path)


def test_add_transactions_writes_new_transaction_to_ledger(app):
    transaction = {
        'type': 'debit',
        'amount': 1099,
        'description': 'Toilet paper (multipack).',
    }
    app.add_transaction(transaction)
    ledger = app.create_ledger()
    ledger.write.assert_called_with(
        [
            {
                'id': 0,
                'date': app.get_date(),
                **transaction,
            }
        ],
        mode='a',
    )


@pytest.mark.parametrize('type, amount', (['foo', 1099], ['debit', 'bar']))
def test_value_error_raised_if_transaction_has_invalid_params(type, amount, app):
    transaction = {
        'type': type,
        'amount': amount,
        'description': 'Stamps',
    }
    with pytest.raises(ValueError):
        app.add_transaction(transaction)


def test_get_transactions_returns_list_of_recorded_transactions(app):
    ledger = app.create_ledger()
    assert app.get_transactions() == ledger.read()


def test_filenotfounderror_gives_id_0(app):
    ledger = app.create_ledger()
    ledger.read.side_effect = FileNotFoundError
    transaction = {'type': 'debit', 'amount': 1099, 'description': 'Soup'}
    app.add_transaction(transaction)
    ledger.write.assert_called_with(
        [{'id': 0, 'date': app.get_date(), **transaction}], mode='a'
    )
