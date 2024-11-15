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
        new_date = request.get_json()['date']
        app.set_date(new_date)
    else:
        return app.get_date()


@api.route('/ledger', methods=['GET', 'PUT'])
def ledger():
    app = get_app()
    if request.method == 'PUT':
        new_ledger = request.get_json()['ledger']
        app.set_ledger(new_ledger)
    else:
        return app.get_ledger()
