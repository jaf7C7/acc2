from unittest.mock import Mock, MagicMock
from argparse import ArgumentError
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
        {'type': command, 'amount': amount, 'description': description}
    )


def test_report_cmd_prints_all_transactions_in_formatted_table(app, capsys):
    app.get_transactions.return_value = [
        {
            'id': 0,
            'date': '2000-01-01',
            'type': 'debit',
            'amount': '1099',
            'description': 'Maltesers',
        },
        {
            'id': 1,
            'date': '2000-01-02',
            'type': 'credit',
            'amount': '999_999_999_999_99',
            'description': 'Gift from Grandma',
        },
    ]
    run(['report'], app=app)
    out, err = capsys.readouterr()
    assert out == (
        'ID      DATE                     AMOUNT  DESCRIPTION\n'
        '0       2000-01-01               -10.99  Maltesers\n'
        '1       2000-01-02  +999,999,999,999.99  Gift from Grandma\n'
    )


@pytest.mark.parametrize(
    'error', (ArgumentError(argument=MagicMock(), message=Mock()), ValueError)
)
def test_exits_with_status_1_if_argument_or_value_error(error, app):
    argv = Mock()
    argv.__getitem__ = Mock(side_effect=error)
    assert run(argv, app=app) == 1


@pytest.mark.parametrize('error', (KeyboardInterrupt, BrokenPipeError))
def test_exits_with_status_2_if_keyboard_interrupt_or_brokenpipe_error(app, error):
    argv = Mock()
    argv.__getitem__ = Mock(side_effect=error)
    assert run(argv, app=app) == 2


def test_exits_with_status_0_if_no_errors(app):
    argv = MagicMock()
    assert run(argv, app=app) == 0
