from acc.cli import parse_args


def test_date_parser_without_new_date():
    args = parse_args(['date'])
    assert args.command == 'date' and args.date is None


def test_date_parser_with_new_date():
    args = parse_args(['date', '2000-01-01'])
    assert args.command == 'date' and args.date == '2000-01-01'
