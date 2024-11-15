from flask import Flask, g, request
from acc.app import Application


api = Flask(__name__)


def get_app():
    if 'app' not in g:
        g.app = Application()
    return g.app


@api.get('/date')
def get_date():
    app = get_app()
    return app.get_date()


@api.put('/date')
def set_date():
    app = get_app()
    new_date = request.get_json()['date']
    app.set_date(new_date)


@api.get('/ledger')
def get_ledger():
    app = get_app()
    return app.get_ledger()


@api.put('/ledger')
def set_ledger():
    app = get_app()
    new_ledger = request.get_json()['ledger']
    app.set_ledger(new_ledger)
