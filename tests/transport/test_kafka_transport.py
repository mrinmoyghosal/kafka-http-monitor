import json

from confluent_kafka.cimpl import KafkaException, KafkaError
from pytest import raises
from pytest_mock import MockerFixture
from transport.kafka_transport import KafkaTransportPublisher, KafkaTransportSync


def test_kafka_transport_publisher(mocker: MockerFixture):
    mocker.patch('transport.kafka_transport.KafkaProducer', autospec=True)
    publisher = KafkaTransportPublisher({})
    publisher.set_topic("topic")
    assert publisher._topic == "topic"
    publisher.publish({"data": "hello"})
    publisher.kafka_producer.produce.assert_called_once_with("topic", json.dumps({"data": "hello"}))
    publisher.kafka_producer.flush.assert_called_once()


def test_kafka_transport_sync(mocker: MockerFixture):
    mocker.patch('transport.kafka_transport.KafkaConsumer', autospec=True)
    logger_patch = mocker.patch('transport.kafka_transport.logger', autospec=True)
    consumer = KafkaTransportSync({})
    consumer.set_topic("topic")
    assert consumer._topic == "topic"

    callback_fn = mocker.MagicMock()

    end_of_partition_msg = mocker.MagicMock()
    end_of_partition_msg.error.return_value.code.return_value = KafkaError._PARTITION_EOF

    valid_msg = mocker.MagicMock()
    valid_msg.error.return_value = False

    error_msg = mocker.MagicMock()
    error_msg.error.return_value.code.return_value = False

    consumer.kafka_consumer.poll.side_effect = [valid_msg, None, end_of_partition_msg, error_msg]
    with raises(KafkaException):
        consumer.consume_message(callback_fn)

    callback_fn.assert_called_once()
    logger_patch.info.assert_called_once_with("No Message found\n")
    logger_patch.error.assert_called_once()

