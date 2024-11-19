from unittest.mock import Mock
import pytest
from acc.cli import run_app


@pytest.fixture
def app():
    return Mock()


def test_run_app_calls_get_date(app):
    args = Mock(command='date', date=None)
    assert run_app(args, app=app) == app.get_date()


def test_run_app_calls_set_date(app):
    args = Mock(command='date', date='2000-01-01')
    run_app(args, app=app)
    app.set_date.assert_called_with('2000-01-01')


def test_run_app_returns_ledger_path(app):
    args = Mock(command='ledger', ledger=None)
    assert run_app(args, app=app) == app.ledger_path


def test_run_app_sets_ledger_path(app):
    args = Mock(command='ledger', ledger='new_ledger')
    run_app(args, app=app)
    assert app.ledger_path == 'new_ledger'


@pytest.mark.parametrize('command', ('debit', 'credit'))
def test_run_app_calls_add_transaction(command, app):
    args = Mock(command=command, amount='1099', description='Marmite')
    run_app(args, app=app)
    app.add_transaction.assert_called_with(
        {'type': command, 'amount': '1099', 'description': 'Marmite'}
    )


def test_run_app_calls_get_transactions(app):
    args = Mock(command='report')
    assert run_app(args, app=app) == app.get_transactions()
