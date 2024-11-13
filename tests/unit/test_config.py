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


def test_getting_date_property_reads_value_from_config_file_if_it_exists():
    config = Config()
    with open(config.path, mode='w') as f:
        f.write('1999-12-31')
    assert config.date == '1999-12-31'
    os.unlink(config.path)
