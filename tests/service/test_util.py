import pytest
from contextlib import contextmanager

from service.util import load_config, CONSTANTS, InvalidConfigException, load_metric_collector_config, \
    load_kafka_config, load_database_config


@contextmanager
def not_raises(Exception):
    try:
        yield
    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")


def test_load_config_load_valid_json():
    with not_raises(Exception):
        load_config('tests/fixtures/test_valid_consumer_config.json', CONSTANTS.CONSUMER)
        load_config('tests/fixtures/test_valid_producer_config.json', CONSTANTS.PRODUCER)


def test_load_config_raises_invalid_config_exception_for_invalid_json_file():
    with pytest.raises(InvalidConfigException):
        load_config('tests/fixtures/test_invalid_consumer_config.json', CONSTANTS.CONSUMER)


def test_load_load_metric_collector_config_work_as_expected():
    config = {
        CONSTANTS.MONITORING_URI: "blah",
        CONSTANTS.HTTP_METHOD: "GET",
        CONSTANTS.REGEX_PATTERN: "python*"
    }
    http_config = load_metric_collector_config(config)
    assert http_config == config


def test_load_kafka_config_work_as_expected():
    input_config = {
        "bootstrap.servers": "aa",
        "ssl.ca.location" : "dfdfdf",
        "ssl.certificate.location": "sfsdf",
        "ssl.key.location": "blahc",
        "security.protocol": "adfadf",
        "ssl.key.location": "adfdf",
        "enable.auto.commit": "adfadf",
        "auto.offset.reset": "adfadf",
        "group.id": "adfadf",
        "auto.commit.interval.ms": ""
    }
    input_config_with_extra= input_config.copy()
    input_config_with_extra.update({"extra": "extra"})
    kafka_config = load_kafka_config(input_config_with_extra)
    assert kafka_config == input_config


def test_load_db_config_work_as_expected():
    input_config = {
        "db_uri": "blachblah"
    }
    input_config_with_extra = input_config.copy()
    input_config_with_extra.update({"extra": "extra"})
    db_config = load_database_config(input_config_with_extra)
    assert db_config == input_config
