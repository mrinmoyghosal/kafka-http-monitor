from confluent_kafka.cimpl import Message

from db.base_database import DatabaseClient
from metrics_collector.base_metric_collector import MetricsCollector
from transport.base_transport import TransportSync, TransportPublisher


class ConsumerRunner:
    """ This class runs the main consumer application """

    def __init__(self, transport: TransportSync, db: DatabaseClient):
        """
        :param transport: a transport object derived from @TransportSync abstract class
        :param db: a database client derived from @DatabaseClient abstract class
        """
        self._transport = transport
        self._db = db

    def run(self):
        """ Run the consumer application with the callback"""
        self._transport.consume_message(self.save_to_db)

    def save_to_db(self, msg: Message):
        """ Callback method saves the data using the db client"""
        self._db.insert_data(msg)


class ProducerRunner:
    """ This class runs the main producer application"""

    def __init__(self, metric_collector: MetricsCollector, transport: TransportPublisher):
        """
        :param metric_collector: a metric_collector object derived from @MetricsCollector abstract class
        :param transport: a transport object derived from @TransportPublisher abstract class
        """
        self._metrics_collector = metric_collector
        self._transport = transport

    async def run(self):
        """ Run the producer and publish the metrics"""
        metrics = await self._metrics_collector.collect_metrics()
        self._transport.publish(metrics)
