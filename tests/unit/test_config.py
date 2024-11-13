import os
from acc.config import Config


def test_default_values_if_config_file_doesnt_exist():
    config = Config()
    assert not os.path.exists(config.path)
    assert config.date == '1970-01-01'
    assert config.ledger == 'ledger'


