# TODO:

- [ ] `cli` module:
    - [ ] `run()`: Calls `_run()`, handles any exceptions, and returns an integer exit code.
    - [ ] `_run()`: Creates an application instance, runs `parse_args(sys.argv[1:])`, calls corresponding `Application` method
- [ ] Make sure methods for all classes are robust against bad inputs etc.
    - [ ] Informative error messages
        - [ ] cli
            - [ ] text via ArgumentParser attrs
            - [ ] appropriate exit codes
        - [ ] flask
            - [ ] text in json response
            - [ ] appropriate status codes
- [ ] Extend transaction reporting (different date ranges, get balance etc.)
- [ ] Write proper README
    - [ ] Usage
    - [ ] Development process (TDD)
    - [ ] Design (SOLID)
