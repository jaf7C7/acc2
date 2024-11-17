from argparse import ArgumentParser


def parse_args(argv):
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    date_parser = subparsers.add_parser('date')
    date_parser.add_argument('date', nargs='?')

    ledger_parser = subparsers.add_parser('ledger')
    ledger_parser.add_argument('ledger', nargs='?')

    return parser.parse_args(argv)
