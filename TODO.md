# TODO:

- [x] Add unit tests for `CSVFile`
- [ ] Make `date` and `ledger_path` non-public attributes of `Application`
- [ ] `cli` module:
    - [ ] `parse_args()`: Parses command-line args
    - [ ] `_run()`: Creates an application instance, runs `parse_args(sys.argv[1:])`, calls corresponding `Application` method
    - [ ] `run()`: Calls `_run()`, handles any exceptions, and returns an integer exit code.
- [x] `api` module:
    - [x] `/date` endpoint:
        - [x] `GET` returns `{'date': <current_date>}`
        - [x] `PUT` accepts json data `{'date': <new_date>}`
    - [x] `/ledger` endpoint:
        - [x] `GET` returns `{'ledger': <current_ledger>}`
        - [x] `PUT` accepts json data `{'ledger': <new_ledger>}`
    - [x] `/transactions` endpoint:
        - [x] `GET` return `{'transactions': <transaction_list>}`
        - [x] `POST` accepts json data `{'type': <type>, 'amount': <amount>, ...}`

- [ ] Make `Application.run()` robust against bad arguments (throw exceptions etc.)
- [x] Put `date` and `ledger_path` properties directly into `Application` class and get rid of `Config` class, `CSVFile` is sufficient.
- [ ] Extend reporting (different date ranges, get balance etc.)
