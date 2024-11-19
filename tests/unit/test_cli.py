from unittest.mock import Mock
import pytest
from acc.app import Application
from acc.cli import run


@pytest.fixture
def app():
    return Mock(spec=Application())


def test_date_cmd_without_new_date_prints_current_date(app, capsys):
    run(['date'], app=app)
    out, err = capsys.readouterr()
    current_date = app.get_date()
    assert out == f'{current_date}\n'


def test_date_cmd_with_new_date_sets_new_date(app):
    new_date = '2000-01-01'
    run(['date', new_date], app=app)
    app.set_date.assert_called_with(new_date)


def test_ledger_cmd_without_new_ledger_prints_current_ledger_path(app, capsys):
    run(['ledger'], app=app)
    out, err = capsys.readouterr()
    current_ledger = app.ledger_path
    assert out == f'{current_ledger}\n'


def test_ledger_cmd_with_new_ledger_sets_new_ledger_path(app):
    new_ledger = 'new_ledger'
    run(['ledger', new_ledger], app=app)
    assert app.ledger_path == new_ledger


@pytest.mark.parametrize('command', ('debit', 'credit'))
def test_debit_and_credit_cmds_with_valid_params_add_new_transaction(command, app):
    amount = '1099'  # Elements of `sys.argv` are always strings.
    description = 'Marmite'
    run([command, amount, description], app=app)
    app.add_transaction.assert_called_with(
        {'type': command, 'amount': int(amount), 'description': description}
    )
