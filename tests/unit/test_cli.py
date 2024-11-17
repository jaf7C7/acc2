from unittest.mock import Mock
import pytest
from acc.cli import parse_args, run_app


@pytest.mark.parametrize(
    'argv, expected_date', ((['date'], None), (['date', '2000-01-01'], '2000-01-01'))
)
def test_date_parser_without_new_date(argv, expected_date):
    args = parse_args(argv)
    assert args.command == 'date' and args.date is expected_date


@pytest.mark.parametrize(
    'argv, expected_ledger',
    ((['ledger'], None), (['ledger', 'new_ledger'], 'new_ledger')),
)
def test_ledger_parser_without_new_ledger(argv, expected_ledger):
    args = parse_args(argv)
    assert args.command == 'ledger' and args.ledger is expected_ledger


@pytest.mark.parametrize('command', ('debit', 'credit'))
def test_transaction_parser(command):
    args = parse_args([command, '1099', 'Maltesers'])
    assert (
        args.command == command
        and args.amount == '1099'
        and args.description == 'Maltesers'
    )


def test_report_parser():
    args = parse_args(['report'])
    assert args.command == 'report'


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
