import json
from json import JSONDecodeError
from typing import Callable

import jsonschema
from jsonschema import ValidationError

from config.schema import consumer_config_schema, producer_config_schema, possible_kafka_parameters


class InvalidConfigException(Exception):
    pass


class CONSTANTS:
    TRANSPORT: str = "transport"
    TOPIC: str = "kafka_topic"
    INTERVAL: str = "interval"
    PRODUCER: str = "producer"
    METRIC_COLLECTOR: str = "metric_collector_type"
    MONITORING_URI: str = "monitoring_uri"
    HTTP_METHOD: str = "http_method"
    HTTP_METHOD_GET: str = "GET"
    REGEX_PATTERN: str = "regex_pattern"
    CONSUMER: str = "CONSUMER"
    DB_HOST: str = "db_uri"


def load_metric_collector_config(config: dict) -> Callable:
    required_params = [CONSTANTS.MONITORING_URI, CONSTANTS.HTTP_METHOD, CONSTANTS.REGEX_PATTERN]
    return {key: config.get(key) for key in required_params if key in config.keys()}


def load_config(file_path: str, type_of_config: str) -> dict:
    try:
        schema = consumer_config_schema if type_of_config == CONSTANTS.CONSUMER else producer_config_schema
        with open(file_path, 'r') as conf_file:
            config = json.loads(conf_file.read())
        jsonschema.validate(config, schema)
        return config
    except (JSONDecodeError, ValidationError) as e:
        raise InvalidConfigException("Malformed config file") from e


def load_kafka_config(config: dict) -> dict:
    kafka_config = {key: config[key] for key in possible_kafka_parameters if key in config.keys()}
    return kafka_config


def load_database_config(config: dict) -> dict:
    required_params = [CONSTANTS.DB_HOST]
    return {key: config.get(key) for key in required_params if key in config.keys()}
