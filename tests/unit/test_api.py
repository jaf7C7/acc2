import pytest
from flask import g
from acc.api import api, get_app
from acc.app import Application


@pytest.fixture
def client():
    return api.test_client()


@pytest.fixture
def app():
    with api.app_context():
        g.app = Application()
        yield g.app


def test_get_app():
    with api.app_context():
        app = get_app()
        assert app is get_app()


def test_get_date_endpoint(app, client):
    assert client.get('/date').get_json() == app.run({'date': ''})
