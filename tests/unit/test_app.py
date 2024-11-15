import pytest
from unittest.mock import MagicMock
from acc.app import Application


@pytest.fixture
def app():
    return Application(config_type=MagicMock(), ledger_type=MagicMock())


def test_empty_date_param_returns_current_date(app):
    app.date = '1970-01-01'
    assert app.run({'date': ''}) == {'date': '1970-01-01'}


def test_non_empty_date_param_sets_new_date(app):
    app.date = '1970-01-01'
    app.run({'date': '1999-12-31'})
    assert app.date == '1999-12-31'


def test_exception_raised_if_new_date_is_not_a_valid_iso_format_date(app):
    with pytest.raises(ValueError):
        app.run({'date': '2000/01/01'})


def test_empty_ledger_param_returns_current_ledger(app):
    app.ledger_path = 'my_ledger'
    assert app.run({'ledger': ''}) == {'ledger': 'my_ledger'}


def test_non_empty_ledger_param_sets_new_ledger(app):
    app.ledger_path = 'old_ledger'
    app.run({'ledger': 'new_ledger'})
    assert app.ledger_path == 'new_ledger'


def test_can_record_transactions(app):
    transaction = {
        'type': 'debit',
        'amount': 1099,
        'description': 'Toilet paper (multipack).',
    }
    app.run({'transaction': transaction})
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
