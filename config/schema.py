producer_config_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "monitoring_uri": "",
            "regex_pattern": "",
            "metric_collector_type": "http",
            "interval": 5,
            "transport": "kafka",
            "bootstrap.servers": "kafka-****-techmaefiker-***.aivencloud.co*:***",
            "kafka_topic": "httpwatcher",
            "ssl.ca.location": "/Users/mghosal/Downloads/ca.pem",
            "ssl.certificate.location": "/Users/mghosal/Downloads/service.cert",
            "ssl.key.location": "/Users/mghosal/Downloads/service.key",
            "security.protocol": "SSL"
        }
    ],
    "required": [
        "monitoring_uri",
        "regex_pattern",
        "interval",
        "metric_collector_type",
        "transport",
        "bootstrap.servers",
        "kafka_topic",
        "ssl.ca.location",
        "ssl.certificate.location",
        "ssl.key.location",
        "security.protocol"
    ],
    "properties": {
        "monitoring_uri": {
            "$id": "#/properties/monitoring_uri",
            "type": "string",
            "title": "The monitoring_uri schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "regex_pattern": {
            "$id": "#/properties/regex_pattern",
            "type": "string",
            "title": "The regex_pattern schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
        },
        "metric_collector_type": {
            "$id": "#/properties/metric_collector_type",
            "type": "string",
            "title": "The metric_collector_type type",
            "description": "An explanation about the purpose of this instance.",
            "default": "http",
            "examples": [
                "http"
            ]
        },
        "interval": {
            "$id": "#/properties/interval",
            "type": "integer",
            "title": "The interval schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                5
            ]
        },
        "transport": {
            "$id": "#/properties/transport",
            "type": "string",
            "title": "The transport schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "kafka"
            ]
        },
        "bootstrap.servers": {
            "$id": "#/properties/bootstrap.servers",
            "type": "string",
            "title": "The bootstrap.servers schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "kafka-1303999d-techkiddy-b03a.aivencloud.com:23908"
            ]
        },
        "kafka_topic": {
            "$id": "#/properties/kafka_topic",
            "type": "string",
            "title": "The kafka_topic schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "httpwatcher"
            ]
        },
        "ssl.ca.location": {
            "$id": "#/properties/ssl.ca.location",
            "type": "string",
            "title": "The ssl.ca.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/ca.pem"
            ]
        },
        "ssl.certificate.location": {
            "$id": "#/properties/ssl.certificate.location",
            "type": "string",
            "title": "The ssl.certificate.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/service.cert"
            ]
        },
        "ssl.key.location": {
            "$id": "#/properties/ssl.key.location",
            "type": "string",
            "title": "The ssl.key.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/service.key"
            ]
        },
        "security.protocol": {
            "$id": "#/properties/security.protocol",
            "type": "string",
            "title": "The security.protocol schema",
            "description": "Define the security protocol to use",
            "default": "",
            "examples": [
                "SSL"
            ]
        }
    },
    "additionalProperties": True
}

consumer_config_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "db_uri": "postgres://user:pass@dbhost:dbport/dbname?sslmode=require",
            "transport": "kafka",
            "bootstrap.servers": "kafka-*****-maefkr-**.aivencloud.com:****",
            "kafka_topic": "httpwatcher",
            "auto.offset.reset": "earliest",
            "group.id": "my-group",
            "enable.auto.commit": "true",
            "auto.commit.interval.ms": "500",
            "ssl.ca.location": "/Users/mghosal/Downloads/ca.pem",
            "ssl.certificate.location": "/Users/mghosal/Downloads/service.cert",
            "ssl.key.location": "/Users/mghosal/Downloads/service.key",
            "security.protocol": "SSL"
        }
    ],
    "required": [
        "db_uri",
        "transport",
        "bootstrap.servers",
        "kafka_topic",
        "auto.offset.reset",
        "group.id",
        "enable.auto.commit",
        "auto.commit.interval.ms",
        "ssl.ca.location",
        "ssl.certificate.location",
        "ssl.key.location",
        "security.protocol"
    ],
    "properties": {
        "db_uri": {
            "$id": "#/properties/db_uri",
            "type": "string",
            "title": "The db_uri schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "postgres://user:pass@dbhost:dbport/dbname?sslmode=require"
            ]
        },
        "transport": {
            "$id": "#/properties/transport",
            "type": "string",
            "title": "The transport schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "kafka"
            ]
        },
        "bootstrap.servers": {
            "$id": "#/properties/bootstrap.servers",
            "type": "string",
            "title": "The bootstrap.servers schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "kafka-1303999d-techkiddy-b03a.aivencloud.com:23908"
            ]
        },
        "kafka_topic": {
            "$id": "#/properties/kafka_topic",
            "type": "string",
            "title": "The kafka_topic schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "httpwatcher"
            ]
        },
        "auto.offset.reset": {
            "$id": "#/properties/auto.offset.reset",
            "type": "string",
            "title": "The auto.offset.reset schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "earliest"
            ]
        },
        "group.id": {
            "$id": "#/properties/group.id",
            "type": "string",
            "title": "The group.id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "my-group"
            ]
        },
        "enable.auto.commit": {
            "$id": "#/properties/enable.auto.commit",
            "type": "string",
            "title": "The enable.auto.commit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "true"
            ]
        },
        "auto.commit.interval.ms": {
            "$id": "#/properties/auto.commit.interval.ms",
            "type": "string",
            "title": "The auto.commit.interval.ms schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "500"
            ]
        },
        "ssl.ca.location": {
            "$id": "#/properties/ssl.ca.location",
            "type": "string",
            "title": "The ssl.ca.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/ca.pem"
            ]
        },
        "ssl.certificate.location": {
            "$id": "#/properties/ssl.certificate.location",
            "type": "string",
            "title": "The ssl.certificate.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/service.cert"
            ]
        },
        "ssl.key.location": {
            "$id": "#/properties/ssl.key.location",
            "type": "string",
            "title": "The ssl.key.location schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "/Users/mghosal/Downloads/service.key"
            ]
        },
        "security.protocol": {
            "$id": "#/properties/security.protocol",
            "type": "string",
            "title": "The security.protocol schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "SSL"
            ]
        }
    },
    "additionalProperties": True
}

possible_kafka_parameters = [
    "bootstrap.servers",
    "ssl.ca.location",
    "ssl.certificate.location",
    "ssl.key.location",
    "security.protocol",
    "ssl.key.location",
    "enable.auto.commit",
    "auto.offset.reset",
    "group.id",
    "auto.commit.interval.ms",
]
