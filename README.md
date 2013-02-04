Benchmark of Python WSGI Servers
================================

Based on:
http://nichol.as/benchmark-of-python-web-servers

We will run the following WSGI application ‘virtuoso_io.py’ on all servers:

::

    # code for ‘virtuoso_io.py


Which performs:
* POST to add a resource
* GET to get a resource

Increasing the rate with an interval of 100 from 400 up to 9000 requests per second for a total of 40.000 requests at each interval.


Contestant servers
------------------

The servers will create / retrieve information in Virtuoso.

These technologies will be used:

* GEvent
* Gunicorn
* Tornado

With and without PyPy.
