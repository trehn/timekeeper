Timekeeper is a library for instrumentation of live Python code by sending measurements to InfluxDB.

Requires Python 2.7 or 3.2+, and InfluxDB 0.9.0+.

Usage
=====

You can use a context manager or decorate a function to record the wall clock time of how long it took that function or block of code to complete:

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

![PyPI downloads](http://img.shields.io/pypi/dm/timekeeper.svg) &nbsp; ![PyPI version](http://img.shields.io/pypi/v/timekeeper.svg) &nbsp; ![Python 2.7](http://img.shields.io/badge/Python-2.7-green.svg) &nbsp; ![Python 3.2+](http://img.shields.io/badge/Python-3.2+-green.svg) &nbsp; ![License](http://img.shields.io/badge/License-ISC-red.svg)
