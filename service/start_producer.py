import argparse
import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config.logger import get_logger
from metrics_collector.http_metric_collector import HttpMetricsCollector
from service.cli_runners import ProducerRunner
from service.util import load_config, CONSTANTS, load_metric_collector_config, load_kafka_config
from transport.kafka_transport import KafkaTransportPublisher

logger = get_logger("service.producer")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Define config file location", default="../producer_config.json")

    payload = parser.parse_args()

    config = load_config(payload.config, CONSTANTS.PRODUCER)
    http_config = load_metric_collector_config(config)
    kafka_config = load_kafka_config(config)

    # initialize metric collector object
    http_metric_collectors = HttpMetricsCollector(http_config)

    # initialize kafka publisher object
    kafka_publisher = KafkaTransportPublisher(kafka_config)
    kafka_publisher.set_topic(config.get(CONSTANTS.TOPIC))

    # initialize the runner
    runner = ProducerRunner(http_metric_collectors, kafka_publisher)

    # Initialize Async Event Scheduler and add producer run function as job with supplied interval
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        runner.run,
        "interval",
        seconds=config.get(CONSTANTS.INTERVAL)
    )

    # Start the scheduler
    scheduler.start()
    logger.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.warning("System Interrupted")


if __name__ == '__main__':
    main()
