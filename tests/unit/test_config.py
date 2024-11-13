import os
from acc.config import Config


def test_returns_default_date_if_config_file_doesnt_exist():
    config = Config()
    assert not os.path.exists(config.path)
    assert config.date == '1970-01-01'


def test_setting_date_property_writes_new_value_to_file():
    config = Config()
    assert not os.path.exists(config.path)
    config.date = '2020-01-01'
    with open(config.path) as f:
        date = f.read()
    assert date == '2020-01-01'
    os.unlink(config.path)
