from flask import Flask, g, request
from acc.app import Application


api = Flask(__name__)


def get_app():
    if 'app' not in g:
        g.app = Application()
    return g.app


@api.route('/<endpoint>', methods=['GET', 'PUT'])
def respond(endpoint):
    app = get_app()
    if request.method == 'PUT':
        args = request.get_json()
    else:
        args = {endpoint: ''}
    return app.run(args)
