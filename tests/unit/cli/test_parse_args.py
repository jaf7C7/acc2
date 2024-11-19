from argparse import ArgumentError
import pytest
from acc.cli import parse_args


@pytest.mark.parametrize(
    'argv, expected_date', ((['date'], None), (['date', '2000-01-01'], '2000-01-01'))
)
def test_date_parser_sets_command_and_date_attrs(argv, expected_date):
    args = parse_args(argv)
    assert args.command == 'date' and args.date is expected_date


@pytest.mark.parametrize(
    'argv, expected_ledger',
    ((['ledger'], None), (['ledger', 'new_ledger'], 'new_ledger')),
)
def test_ledger_parser_sets_command_and_ledger_attrs(argv, expected_ledger):
    args = parse_args(argv)
    assert args.command == 'ledger' and args.ledger is expected_ledger


@pytest.mark.parametrize('command', ('debit', 'credit'))
def test_transaction_parser_sets_command_amount_and_description_attrs(command):
    args = parse_args([command, '1099', 'Maltesers'])
    assert (
        args.command == command
        and args.amount == 1099
        and args.description == 'Maltesers'
    )


def test_non_integer_debit_amount_raises_argument_error():
    with pytest.raises(ArgumentError):
        parse_args(['debit', 'ten ninety nine', 'Maltesers'])


def test_report_parser_sets():
    args = parse_args(['report'])
    assert args.command == 'report'
