import time

import aiohttp

from metrics_collector.base_metric_collector import MetricsCollector


class HttpMetricsCollector(MetricsCollector):
    """ HTTP based metric collector implementation"""

    def __init__(self, config):
        super().__init__(config)

    async def collect_metrics(self) -> dict:
        """ Collect the data from HTTP endpoint """
        async with aiohttp.ClientSession() as session:
            start = time.time()
            async with session.get(self._http_endpoint) as response:
                html = await response.text()
                pattern_found = False
                if self._regex_pattern and self._compiled_regex.match(html):
                    pattern_found = True

                end = time.time()
                data = {
                    "address": self._http_endpoint,
                    "response_status": response.status,
                    "response_time_in_seconds": end - start,
                    "content_type": response.headers['content-type'],
                    "regex_pattern_found": pattern_found,
                    "regex_pattern": self._regex_pattern
                }
                return data
