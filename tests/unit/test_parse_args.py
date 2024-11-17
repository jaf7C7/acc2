import pytest
from acc.cli import parse_args


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
