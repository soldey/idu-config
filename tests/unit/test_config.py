import os

import pytest

from iduconfig.config import Config


@pytest.fixture(scope="function")
def prepare_env():
    config = Config()
    yield config


def test_get_existing_env(prepare_env):
    key = "TEST1"
    assert prepare_env.get(key) == "123"


def test_get_non_existing_env(prepare_env):
    key = "TEST_NON_EXISTING"
    with pytest.raises(ValueError) as e:
        prepare_env.get(key)
        assert key in e.value


def test_set_env(prepare_env):
    key = "TEST1"
    prepare_env.set(key, "new val")
    assert prepare_env.get(key) == "new val"


def test_load_non_existing_env():
    os.environ["APP_ENV"] = ""
    with pytest.raises(ValueError) as e:
        _ = Config()
    os.environ["APP_ENV"] = "non_existing"
    with pytest.raises(FileNotFoundError) as e:
        _ = Config()
