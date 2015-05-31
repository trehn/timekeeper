from contextlib import contextmanager
from datetime import datetime
from functools import wraps

from influxdb import InfluxDBClient


@contextmanager
def timekeeper_context(tk, measurement, tags):
    start = datetime.now()
    yield
    end = datetime.now()
    tk.submit_measurement(
        measurement,
        (end - start).total_seconds(),
        tags,
    )


class TimeKeeper(object):
    def __init__(self, dsn, prefix="", tags=None, **kwargs):
        self.connection = InfluxDBClient.from_DSN(dsn, **kwargs)
        self.prefix = prefix
        self.tags = {} if tags is None else tags

    def context(self, measurement, tags=None):
        tags = {} if tags is None else tags
        return timekeeper_context(self, measurement, tags)

    def decorate(self, measurement, tags=None):
        def outer(func):
            @wraps(func)
            def inner(*args, **kwargs):
                with self.context(measurement, tags=tags):
                    return func(*args, **kwargs)
            return inner
        return outer

    def submit_measurement(self, measurement, value, tags):
        self.connection.write_points(
            [{
                "fields": {
                    "value": value,
                },
                "name": self.prefix + measurement,
                "tags": tags,
            }],
            tags=self.tags,
        )
