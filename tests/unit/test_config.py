import os
from acc.config import Config


def test_returns_default_date_if_config_file_doesnt_exist():
    config = Config()
    assert not os.path.exists(config.path)
    assert config.get_date() == '1970-01-01'
