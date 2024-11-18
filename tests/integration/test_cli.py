from unittest.mock import Mock
import pytest
import acc.cli as cli


def test_get_date(capsys):
    cli.run(['date'])
    out, err = capsys.readouterr()
    assert out == '1970-01-01\n'
