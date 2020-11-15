import asyncio
from unittest.mock import MagicMock

from pytest_mock import MockerFixture
from service.cli_runners import ConsumerRunner, ProducerRunner


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


def test_consumer_runner_call_consume_message(mocker: MockerFixture):
    transport = mocker.MagicMock()
    transport.consume_message = mocker.MagicMock()
    db = mocker.MagicMock()
    runner = ConsumerRunner(transport, db)
    runner.run()
    transport.consume_message.assert_called_once()


def test_producer_runner_call_consume_message(mocker: MockerFixture):
    metric_collector = mocker.MagicMock()
    metric_collector.collect_metrics = AsyncMock()
    data = {"data": "blah"}
    metric_collector.collect_metrics.return_value = data

    transport = mocker.MagicMock()
    transport.publish = mocker.MagicMock()

    runner = ProducerRunner(metric_collector, transport)
    asyncio.get_event_loop().run_until_complete(runner.run())
    metric_collector.collect_metrics.assert_called_once()
    transport.publish.assert_called_once_with(data)
