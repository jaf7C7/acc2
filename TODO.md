# TODO:

- [ ] Make API recieve data of type `application/x-www-form-urlencoded` and send data of type `application/json`
- [ ] Make the API RESTful! e.g. *statelessness* requires the server to treat each request as a brand new client, so `date` and `ledger` values must be added to each request.
    - See <https://restfulapi.net/> for REST constraints
    - See the [Stripe API](https://docs.stripe.com/api/balance/balance_object?lang=curl)  for example requests and responses
    - Consider implementing [pagination](https://docs.stripe.com/api/pagination?lang=curl)
    - Nice informative [errors](https://docs.stripe.com/api/errors)
    - [ ] `/ledgers`
        - [ ] `GET`: list of available ledgers

            ```json
            {
                "object": "list",
                "url": "/ledgers",
                "data": [
                    {
                        "object": "ledger",
                        "id": "ledger_...",
                        "url": "/ledgers/0",
                        ...
                    },
                    ...
                ],
            }
            ```
        - [ ] `POST`: add new ledger
            - [ ] `application/x-www-form-urlencoded` key-value pairs:
                - `name=<name>`
    - [ ] `/ledger/<id>`
        - [ ] GET: ledger metadata

            ```json
            {
                "object": "ledger",
                "id": "ledger_..."
                "name": "...",
                "created": "<time in seconds since unix epoch>",
                "transactions": {
                    "count": 5,
                    "url": "/ledgers/0/transactions",
                }
            }
            ```
    - [ ] `/ledger/<id>/transactions`
        - [ ] `GET`: list of transactions
            - Parameters in the query string refine search:
                - `created=YYYY-MM-DDTHH:MM:SSZ` (iso timestamp)
                    - can omit e.g. `:SS` to get whole hour, or omit everything but `YYYY` for whole year etc.
                - `created_after=<timestamp>`
                - `created_before=<timestamp>`
                - `type=<debit or credit>`
                - `amount=<amount>`
                - `amount_less_than=<amount>`
                - `amount_more_than=<amount>`
                - `description=<simple text match>`

            ```json
            {
                "object": "list",
                "url": "/ledger/<id>/transactions",
                "data": [
                    {
                        "object": "transaction",
                        "id": "transaction_...",
                        ...
                    },
                ],
            }
            ```
        - [ ] `POST`: add a transaction
            - [ ] `application/x-www-form-urlencoded` key-value pairs:
                - `type=<type>`
                - `amount=<amount>`
                - `description=<description>`
    - [ ] `/ledger/<id>/balance`
        - [ ] `GET`: Calculate balance of entire ledger

            ```json
            {
                "object": "balance",
                "ledger": "<ledger id>"
                "available": "<integer amount>",
                "calculated": "<date in seconds since epoch>",
            }
            ```
    - [ ] `/ledger/<id>/transactions/<id>`
        - [ ] `GET`: transaction object

            ```json
            {
                "object": "transaction",
                "id": "transaction_...",
                "ledger": "<ledger id>",
                "created": "<date in seconds since unix epoch>",
                "type": "<debit or credit>"
                "amount": "<integer amount in smallest units of currency>",
                "description": "...",
            }
            ```
- [ ] look at API UX
    - [ ] GET to `/` analogous to `--help`? lists endpoints and methods
    - [ ] OPTIONS to any endpoint (including `/` returns accepted methods (look into best practices)
- [ ] Add option to use a database instead of a csvfile
- [ ] Redesign the CLI to work with the API
- [ ] Informative error messages
    - [ ] cli
        - [ ] help text via ArgumentParser attrs
        - [ ] appropriate exit codes
    - [ ] flask
        - [ ] appropriate status codes
        - [ ] appropriate message format.  See <https://www.baeldung.com/rest-api-error-handling-best-practices#2-default-spring-error-responses>
- [ ] CLI: Use `tabulate` (pip install tabulate) for table generation
- [ ] Write proper README
    - [ ] Usage
    - [ ] Development process (TDD)
    - [ ] Design (SOLID)
