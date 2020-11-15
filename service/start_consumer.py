import argparse

from config.logger import get_logger
from db.postgres_db import PgDatabaseClient
from service.cli_runners import ConsumerRunner
from service.util import load_config, CONSTANTS, load_database_config, load_kafka_config
from transport.kafka_transport import KafkaTransportSync

logger = get_logger("service.consumer")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--config", help="Define the config file ", default="../consumer_config.json")
    payload = parser.parse_args()

    config = load_config(payload.config, CONSTANTS.CONSUMER)
    db_config = load_database_config(config)
    kafka_config = load_kafka_config(config)

    # initialize db client instance
    db_client = PgDatabaseClient(db_config)

    # initialize kafka consumer instance
    kafka_consumer = KafkaTransportSync(kafka_config)
    kafka_consumer.set_topic(config.get(CONSTANTS.TOPIC))

    # Initialize the Consumer runner
    runner = ConsumerRunner(kafka_consumer, db_client)
    try:
        runner.run()
    except (KeyboardInterrupt, SystemExit):
        logger.warn("System Interrupted")


if __name__ == '__main__':
    main()
