import abc
from typing import Callable


class Transport(abc.ABC):
    """ Base transport entity"""
    _config: dict

    @abc.abstractmethod
    def __init__(self, config: dict):
        self._config = config
        self.configure()

    @abc.abstractmethod
    def configure(self):
        pass


class TransportPublisher(Transport):
    """ Base transport publisher """

    @abc.abstractmethod
    def publish(self, metric):
        pass


class TransportSync(Transport):
    """ Base transport consumer """

    @abc.abstractmethod
    def consume_message(self, callback_fn: Callable):
        pass
