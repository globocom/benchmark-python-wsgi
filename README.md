Benchmark of Python WSGI Servers
================================

We were interested in comparing Gevent with Tornado to see which would better suit our needs.
The starting point was a [benchmark  done by Nicholas Piël in 2010](http://nichol.as/benchmark-of-python-web-servers)
showing that Tornado had excellent performance followed closely by Gevent.

We did a very quick and non-rigorous benchmark in 2013-01-05.
Nevertheless we are making the code and results available in case this can be useful elsewhere.


Scenarios
---------

First we tested a linux client generating HTTP traffic towards a MacOSX running the server backend. 
This test was run over the corporate wi-fi network.
Then, we recreated the same test scenario in two different sets of Amazon instances to cross-validate the performance 
measured.

In the client side, we used [wrk](https://github.com/wg/wrk), 
[weighttp](http://redmine.lighttpd.net/projects/weighttp/wiki) and 
[locust](http://locust.io/) to generate traffic.

The test cases where basically: 
  - the HTTP server just responds a "hello world" to a GET request.
  - the HTTP server queries a backend Virtuoso triple-store database 
  - the HTTP server queries a backend REDIS database

Infra-structure details
-----------------------

In the tests were used:
 * (corporate) Linux running Fedora 16, Intel(R) Core(TM) i7-2640M CPU @ 2.80GHz 8Gb RAM, cache size 4096 KB 
 * (corporate) MacOSX lion 10.7.5 - 2Ghz Intel Vore i5 8Gb RAM, L2 Cache (per Core) 256 KB
 * (Amazon)  Linux Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-31-virtual x86_64), Intel(R) Xeon(R) CPU E5645  @ 2.40GHz, cache size 12288 KB 
 
Results
--------

<div>
 <script src="http://code.highcharts.com/highcharts.js"></script>
 <div id="container" style="height: 400px"></div>
</div>


 [This file](https://github.com/globocom/benchmark-python-wsgi/blob/master/Benchmarks.md) contains dumps of the tests executed.
 

Team members
------------

The team members that took part in the testing efforts were:

  - Guilherme Machado Cirne
  - Ícaro Medeiros
  - Rodrigo Dias Arruda Senra
  - Tatiana Al-Chuery Pereira Martins

 
References
----------

 * [1] http://nichol.as/benchmark-of-python-web-servers
 * [2] https://github.com/wg/wrk
 * [3] http://redmine.lighttpd.net/projects/weighttp/wiki
 * [4] http://locust.io/
 * [5] https://github.com/bobhancock/Pycon-2012-Parallelism-and-Concurrency

