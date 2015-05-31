Timekeeper is a library for instrumentation of live Python code by sending measurements to InfluxDB.

Requires Python 2.7 or 3.2+, and InfluxDB 0.9.0+.

Usage
=====

```python
from timekeeper import TimeKeeper

tk = TimeKeeper(
    "udp+influxdb://localhost/databasename",
    prefix="location-1.cluster-1.app-1.",  # if you prefer Graphite style over tags
    tags={"host": "location-1.cluster-1.app-1"},
)


@tk.decorate("some_slow_function", tags={"foo": "bar"})
def slowpoke():
    sleep(9001)


def slowpoke2():
    with tk.context("some_other_slow_function", tags={"foo": "baz"}):
        sleep(9001)
```

Installation
============

```
pip install timekeeper
```
