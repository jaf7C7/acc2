from flask import Flask, g, request
from acc.app import Application


api = Flask(__name__)


def get_app():
    if 'app' not in g:
        g.app = Application()
    return g.app


@api.route('/date', methods=['GET', 'PUT'])
def date():
    app = get_app()
    if request.method == 'PUT':
        new_date = request.form['date']
        app.set_date(new_date)
    else:
        return {'date': app.get_date()}


@api.route('/ledger', methods=['GET', 'PUT'])
def ledger():
    app = get_app()
    if request.method == 'GET':
        return {'ledger': app.ledger_path}
    elif request.method == 'PUT':
        new_ledger = request.get_json()['ledger']
        app.ledger_path = new_ledger


@api.route('/transactions', methods=['GET', 'POST'])
def transactions():
    app = get_app()
    if request.method == 'GET':
        transactions = app.get_transactions()
        return {'transactions': transactions}
    elif request.method == 'POST':
        transaction = request.get_json()
        app.add_transaction(transaction)
