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
