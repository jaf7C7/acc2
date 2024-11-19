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
        template = '{:<6}  {:10}  {:>8}  {}'
        header = None
        for transaction in app.get_transactions():
            transaction['amount'] = int(transaction['amount']) / 100
            if transaction.pop('type') == 'debit':
                transaction['amount'] *= -1
            if header is None:
                header = transaction.keys()
                print(template.format(*header).upper())
            print(template.format(*transaction.values()))


def run(*args, **kwargs):
    try:
        _run(*args, **kwargs)
    except ArgumentError:
        return 1
    except (BrokenPipeError, KeyboardInterrupt):
        return 2
    else:
        return 0
