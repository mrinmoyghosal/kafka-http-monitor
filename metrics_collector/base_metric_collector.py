import re
from abc import ABC, abstractmethod

from service.util import CONSTANTS


class MetricsCollector(ABC):
    """ Base metric collector api"""
    _config: dict

    @abstractmethod
    def __init__(self, config: dict):
        self._config = config
        self._http_endpoint = self._config.get(CONSTANTS.MONITORING_URI)
        self._http_method = self._config.get(CONSTANTS.HTTP_METHOD, CONSTANTS.HTTP_METHOD_GET)
        if self._config.get(CONSTANTS.REGEX_PATTERN, ""):
            self._regex_pattern = self._config.get(CONSTANTS.REGEX_PATTERN)
            self._compiled_regex = re.compile(self._regex_pattern)

    @abstractmethod
    async def collect_metrics(self) -> dict:
        """ Abstact method for collecting metrics"""
        pass
