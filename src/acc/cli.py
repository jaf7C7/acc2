from argparse import ArgumentParser, ArgumentError


def _parse_args(argv):
    parser = ArgumentParser(exit_on_error=False)
    subparsers = parser.add_subparsers(dest='command')

    date_parser = subparsers.add_parser('date', exit_on_error=False)
    date_parser.add_argument('date', nargs='?')

    ledger_parser = subparsers.add_parser('ledger')
    ledger_parser.add_argument('ledger', nargs='?')

    transaction_parser = ArgumentParser(add_help=False)
    transaction_parser.add_argument('amount', type=int)
    transaction_parser.add_argument('description')

    debit_credit_parser = subparsers.add_parser(
        'debit', aliases=['credit'], parents=[transaction_parser], exit_on_error=False
    )

    report_parser = subparsers.add_parser('report')

    return parser.parse_args(argv)


def _tabulate(transactions):
    fields = {
        'id': '{:<6}',
        'date': '{:10}',
        'amount': '{:>8}',
        'description': '{}',
    }
    template = '  '.join(fields.values())
    yield template.format(*fields.keys()).upper()
    for transaction in transactions:
        transaction['amount'] = int(transaction['amount']) / 100
        if transaction.pop('type') == 'debit':
            transaction['amount'] *= -1
        transaction['amount'] = '{:.2f}'.format(transaction['amount'])
        yield template.format(*transaction.values())


def _run(argv, app):
    args = _parse_args(argv)
    if args.command == 'date':
        if args.date is not None:
            app.set_date(args.date)
        else:
            print(app.get_date())

    elif args.command == 'ledger':
        if args.ledger is not None:
            app.ledger_path = args.ledger
        else:
            print(app.ledger_path)

    elif args.command in ('credit', 'debit'):
        transaction = {
            'type': args.command,
            'amount': args.amount,
            'description': args.description,
        }
        app.add_transaction(transaction)

    elif args.command == 'report':
        for row in _tabulate(app.get_transactions()):
            print(row)


def run(*args, **kwargs):
    try:
        _run(*args, **kwargs)
    except (ArgumentError, ValueError):
        return 1
    except (BrokenPipeError, KeyboardInterrupt):
        return 2
    else:
        return 0
