import pytest
from acc.api import api


@pytest.fixture
def client():
    return api.test_client()


def test_get_date_endpoint(client):
    assert client.get('/date').get_json() == {'date': '1970-01-01'}
