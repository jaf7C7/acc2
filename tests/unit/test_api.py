from unittest.mock import MagicMock
import pytest
from flask import g
from acc.api import api, get_app


@pytest.fixture
def client():
    return api.test_client()


@pytest.fixture
def app():
    with api.app_context():
        g.app = MagicMock()
        yield g.app


def test_get_app():
    with api.app_context():
        app = get_app()
        assert app is get_app()


def test_get_date_endpoint(app, client):
    client.get('/date')
    app.run.assert_called_with({'date': ''})
