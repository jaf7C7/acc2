# TODO:

- [ ] `cli` module:
    - [ ] `parse_args()`: Parses command-line args into a dict consumable by `Application.run()`
    - [ ] `run()`: Creates an application instance, runs `parse_args(sys.argv[1:])`,
      and passes that to `Application.run()`, handles any exceptions, and returns
      an integer.
- [ ] `api` module:
    - [ ] `/date` endpoint:
        - [ ] `GET` return `{'date': <current_date>}`
        - [ ] `PUT` `appliation/x-www-form-urlencoded` form data `{'date': <new_date>}`
    - [ ] `/ledger` endpoint:
        - [ ] `GET` return `{'ledger': <current_ledger>}`
        - [ ] `PUT` `application/x-www-form-urlencoded` form data `{'ledger': <new_ledger>}`
    - [ ] `/transactions` endpoint:
        - [ ] `GET` return `{'transactions': <transaction_list>}` (depending on `application/x-www-form-urlencoded` form data to refine transaction list.
        - [ ] `POST` new transaction `{'type': <debit_or_credit>, 'amount': <amount>, 'description': <description>}`

- [ ] Make `Application.run()` robust against bad arguments (throw exceptions etc.)
- [ ] Extend reporting (different date ranges, get balance etc.)