from unittest.mock import Mock
import pytest
from acc.app import Application
from acc.cli import run


@pytest.fixture
def app():
    return Mock(spec=Application())


def test_date_cmd_without_new_date_prints_current_date(app, capsys):
    run(['date'], app=app)
    out, err = capsys.readouterr()
    current_date = app.get_date()
    assert out == f'{current_date}\n'


def test_date_cmd_with_new_date_sets_new_date(app):
    new_date = '2000-01-01'
    run(['date', new_date], app=app)
    app.set_date.assert_called_with(new_date)
