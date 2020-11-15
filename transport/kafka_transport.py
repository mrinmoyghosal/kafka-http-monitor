import json
import time

from confluent_kafka import (
    Producer as KafkaProducer,
    Consumer as KafkaConsumer
)
from confluent_kafka.cimpl import KafkaError, KafkaException

from config.logger import get_logger
from transport.base_transport import TransportPublisher, TransportSync

logger = get_logger("kafka_transport")


class KafkaTransportPublisher(TransportPublisher):
    """ TransportPublisher implementation using Kafka"""

    def __init__(self, config: dict):
        super().__init__(config)

    def set_topic(self, topic: str):
        self._topic = topic

    def configure(self) -> None:
        self.kafka_producer = KafkaProducer(self._config)

    def publish(self, metric: dict) -> None:
        self.kafka_producer.produce(self._topic, json.dumps(metric))
        self.kafka_producer.flush()
        logger.info(f"Published METRIC: {metric} at {time.monotonic()}")


class KafkaTransportSync(TransportSync):
    """ TransportSync implementation using kafka"""

    def __init__(self, config: dict):
        super().__init__(config)

    def configure(self) -> None:
        self.kafka_consumer = KafkaConsumer(self._config)

    def set_topic(self, topic: str):
        self._topic = topic

    def consume_message(self, callback_fn):
        try:
            self.kafka_consumer.subscribe([self._topic])
            self.running = True

            while self.running:
                msg = self.kafka_consumer.poll(timeout=1.0)
                if msg is None:
                    logger.info("No Message found\n")
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        logger.error('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    callback_fn(msg.value())
        finally:
            # Close down consumer to commit final offsets.
            self.kafka_consumer.close()
            self.running = False
