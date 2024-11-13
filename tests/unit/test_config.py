import os
import pytest
from acc.config import Config


@pytest.fixture
def config(tmp_path):
    config_path = os.path.join(tmp_path, 'test_config')
    config = Config(config_path)
    yield config
    try:
        os.unlink(config_path)
    except FileNotFoundError:
        pass


def test_default_values_if_config_file_doesnt_exist(config):
    assert not os.path.exists(config.path)
    assert config.date == '1970-01-01'
    assert config.ledger == 'ledger'


def test_state_is_persistent_between_config_instances(config):
    config.date = '2020-01-01'
    config.ledger = 'new_ledger'
    other_config = Config()
    assert not other_config.date == config.date
    other_config.path = config.path
    assert other_config.date == config.date and other_config.ledger == config.ledger
