from flask import Flask
from acc.app import Application


api = Flask(__name__)


@api.route('/date')
def get_date():
    app = Application()
    return app.run({'date': ''})
