from unittest.mock import Mock
import pytest
from acc.cli import run_app


@pytest.fixture
def app():
    return Mock()


def test_date_cmd_without_new_date_prints_current_date(app, capsys):
    args = Mock(command='date', date=None)
    run_app(args, app=app)
    out, err = capsys.readouterr()
    assert out == f'{app.get_date()}\n'


def test_run_app_calls_set_date(app):
    args = Mock(command='date', date='2000-01-01')
    run_app(args, app=app)
    app.set_date.assert_called_with('2000-01-01')


def test_ledger_cmd_without_new_ledger_prints_current_ledger_path(app, capsys):
    args = Mock(command='ledger', ledger=None)
    run_app(args, app=app)
    out, err = capsys.readouterr()
    assert out == f'{app.ledger_path}\n'


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


def test_report_cmd_prints_all_transactions(app, capsys):
    args = Mock(command='report')
    run_app(args, app=app)
    out, err = capsys.readouterr()
    assert out == f'{app.get_transactions()}\n'
