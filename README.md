![develop](https://github.com/mrinmoyghosal/kafka-http-monitor/workflows/build/badge.svg?branch=develop)

# Kafka based HTTP monitor

## Prerequisites
* Python 3.9
* librdkafka

#### Install librdkafka
```
brew install librdkafka  # Macos
apt-get install librdkafka-dev  # Ubuntu 
```

## Installation
```
python setup.py install
```
## Run the producer application
```
start_producer --config config_file_path.json
```
## Run the consumer application
```
start_consumer --config config_file_path.json
```

## Build and run using docker
```
docker build -t kafka_http_monitor .
```
## Run consumer and producer from docker image
```
docker run -v local_config_path.json:container_config_path.json -it kafka_http_monitor start_consumer --config container_config_path.json
docker run -v local_config_path.json:container_config_path.json -it kafka_http_monitor start_producer --config container_config_path.json

```
## JSON Schema for input validation

[jsonschema for configuration file ](config/schema.py)

## Example Consumer Config
```json
{
  "db_uri": "postgres://user:pass@dbhost:dbport/defaultdb?sslmode=require",
  "transport": "kafka",
  "bootstrap.servers": "localhost",
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
```
## Example Producer Config
```json
{
  "monitoring_uri": "https://www.python.org",
  "regex_pattern": "python",
  "interval": 5,
  "transport": "kafka",
  "metric_collector_type": "http",
  "bootstrap.servers": "localhost:23908",
  "kafka_topic": "httpwatcher",
  "ssl.ca.location": "/Users/mghosal/Downloads/ca.pem",
  "ssl.certificate.location": "/Users/mghosal/Downloads/service.cert",
  "ssl.key.location": "/Users/mghosal/Downloads/service.key",
  "security.protocol": "SSL"
}
```

## Development

### Setup development environment
```
pip install poetry==1.1.4
cd kafka-http-monitor
poetry install
```
### Run test
```
poetry run pytest
```
