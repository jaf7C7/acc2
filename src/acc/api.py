from flask import Flask, g
from acc.app import Application


api = Flask(__name__)


def get_app():
    if 'app' not in g:
        g.app = Application()
    return g.app


@api.route('/date')
def get_date():
    app = get_app()
    return app.run({'date': ''})
