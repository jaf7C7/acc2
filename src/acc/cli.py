from argparse import ArgumentParser


def parse_args(argv):
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    date_parser = subparsers.add_parser('date')
    date_parser.add_argument('date', nargs='?')

    ledger_parser = subparsers.add_parser('ledger')
    ledger_parser.add_argument('ledger', nargs='?')

    transaction_parser = ArgumentParser(add_help=False)
    transaction_parser.add_argument('amount')
    transaction_parser.add_argument('description')

    debit_credit_parser = subparsers.add_parser(
        'debit', aliases=['credit'], parents=[transaction_parser]
    )

    return parser.parse_args(argv)


def run_app(args, app):
    if args.command == 'date':
        if args.date is not None:
            app.set_date(args.date)
        else:
            return app.get_date()
    elif args.command == 'ledger':
        if args.ledger is not None:
            app.ledger_path = args.ledger
        else:
            return app.ledger_path
