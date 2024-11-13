"""Test the integration of the Application and Config objects."""

from acc.app import Application


def test_empty_date_param_returns_default_date():
    app = Application()
    assert app.run({'date': ''}) == {'date': '1970-01-01'}
