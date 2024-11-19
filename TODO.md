# TODO:

- [ ] Make sure methods for all classes are robust against bad inputs etc.
    - [ ] Do all data validation in `Application` not in `cli` or `api`
        - [ ] Check transaction `amount` validity with `str.isnumeric()` (maybe)
        - [ ] Allow `amount` arguments of the form `10.99` and convert and store them as `1099`.
        - [ ] Check date validity with `date.fromisoformat()`
    - [ ] Informative error messages
        - [ ] cli
            - [ ] help text via ArgumentParser attrs
            - [ ] appropriate exit codes
        - [ ] flask
            - [ ] help text in json response
            - [ ] appropriate status codes
- [ ] Add option to use a database instead of a csvfile
- [ ] Extend transaction reporting (different date ranges, get balance etc.)
- [ ] Write proper README
    - [ ] Usage
    - [ ] Development process (TDD)
    - [ ] Design (SOLID)
