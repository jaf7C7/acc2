import pytest
from acc.api import api
from acc.app import Application


@pytest.fixture
def client():
    return api.test_client()


def test_get_date_endpoint(client):
    app = Application()
    assert client.get('/date').get_json() == app.run({'date': ''})
