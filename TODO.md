# TODO:

- [ ] `cli` module:
    - [ ] `parse_args()`: Parses command-line args
    - [ ] Add `credit` and `debit` parsers:
        - [ ] Want `acc [debit|credit] <amount> <description>`
        - [ ] Fails if `amount` or `description` missing
        - [ ] Should set `args.transaction = {
                  'type': <debit|credit>, 'amount': <amount>, 'description': <description>
              }`
    - [ ] `run()`: Calls `_run()`, handles any exceptions, and returns an integer exit code.
    - [ ] `_run()`: Creates an application instance, runs `parse_args(sys.argv[1:])`, calls corresponding `Application` method
- [ ] Make sure methods for all classes are robust against bad inputs etc.
- [ ] Extend transaction reporting (different date ranges, get balance etc.)
- [ ] Write proper README
    - [ ] Usage
    - [ ] Development process (TDD)
    - [ ] Design (SOLID)
