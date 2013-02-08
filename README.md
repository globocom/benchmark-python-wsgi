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

In the tests we used the following hardware configuration:
 * (corporate) Linux running Fedora 16, Intel(R) Core(TM) i7-2640M CPU @ 2.80GHz 8Gb RAM, cache size 4096 KB 
 * (corporate) MacOSX lion 10.7.5 - 2Ghz Intel Vore i5 8Gb RAM, L2 Cache (per Core) 256 KB
 * (Amazon)  Linux Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-31-virtual x86_64), Intel(R) Xeon(R) CPU E5645  @ 2.40GHz, cache size 12288 KB 


Results
--------

The test cases were:

 * tornado_lan_flask_hw - Tornado returning a simple "Hello World" for GET /  with Flask in corporate network
 * tornado_lan_sock_hw - Tornado returning a simple "Hello World" for GET /  with pure sockets in corporate network 
 * tornado_virt_lan - Tornado doing a query in Virtuoso (all servers in the same machine) in corporate network
 * tornado_virt_s3 - Tornado doing a query in Virtuoso (all servers in the same machine) in Amazon Srv3
 * tornado_virt_s1s2_pycurl - Tornado doing a query in Virtuoso (servers in different machines) in Amazon Srv1-Srv2
 * tornado_virt_s1s2_native - Tornado doing a query in Virtuoso (servers in different machines) in Amazon Srv1-Srv2 (without PyCurl)
 * tornado_virt_pypy - Tornado doing a query in Virtuoso (servers in different machines) in Amazon Srv1-Srv2 (over Pypy)
 * tornado_inc_load - Tornado incremental load

 * gevent_lan_flask_hw - Gevent returning a simple "Hello World" for GET /  with Flask in corporate network
 * gevent_lan_sock_hw - Gevent returning a simple "Hello World" for GET /  with pure sockets in corporate network
 * gevent_pure_wsgi - Gevent returning a simple "Hello World" for GET /  with pure WSGI in corporate network
 * gevent_virt_lan - Gevent doing a query in Virtuoso (all servers in the same machine) in corporate network
 * gevent_virt_s3 - Gevent doing a query in Virtuoso (all servers in the same machine) in Amazon Srv3
 * gevent_virt_s3_alt - Gevent (alternate implementaion) doing a query in Virtuoso (all servers in the same machine) in Amazon Srv3
 * gevent_virt_s1s2 - Gevent doing a query in Virtuoso (servers in different machines) in Amazon Srv1-Srv2 
 * gevent_virt_s1s2_alt - Gevent doing a query in Virtuoso (servers in different machines) in Amazon Srv1-Srv2 
 * gevent_inc_load - Gevent incremental load
 * gevent_inc_load_alt - Gevent incremental load (alternate implementaion)

The table below depicts the average results for comparison: 
 
<table>
  <tr>
    <th>Test Case</th> <th>Runs</th> <th>Avg. Requests/s</th>  <th>Max Requests/s</th>  <th>Min Requests/s</th>
  </tr>
  <tr>
    <td>tornado_lan_flask_hw</td> <td>10</td> <td>1929.68</td> <td>2186.74</td> <td>1395.3</td>
  </tr>
  <tr>
    <td>gevent_lan_flask_hw</td> <td>5</td> <td>883.21</td> <td>941.02</td> <td>791.95</td>
  </tr>
  <tr>
    <td>tornado_lan_sock_hw</td> <td>2</td> <td>5723.74</td> <td>5731.39</td> <td>5716.09</td>
  </tr>
  <tr>
    <td>gevent_lan_sock_hw</td> <td>2</td> <td>6597.43</td> <td>6617.0</td> <td>6577.87</td>
  </tr>
  <tr>
    <td>gevent_pure_wsgi</td> <td>3</td> <td>3652.08</td> <td>3906.9</td> <td>3404.44</td>
  </tr>
  <tr>
    <td>tornado_virt_lan</td> <td>4</td> <td>643.21</td> <td>740.14</td> <td>377.55</td>
  </tr>
  <tr>
    <td>gevent_virt_lan</td> <td>6</td> <td>140.12</td> <td>162.46</td> <td>130.91</td>
  </tr>
  <tr>
    <td>tornado_virt_s3</td> <td>5</td> <td>900.48</td> <td>920.0</td> <td>881.46</td>
  </tr>
  <tr>
    <td>gevent_virt_s3</td> <td>4</td> <td>436.85</td> <td>449</td> <td>428.79</td>
  </tr>
  <tr>
    <td>gevent_virt_s3_alt</td> <td>4</td> <td>522.32</td> <td>525</td> <td>516</td>
  </tr>
  <tr>
    <td>tornado_virt_s1s2_pycurl</td> <td>2</td> <td>986</td> <td>991</td> <td>981</td>
  </tr>
  <tr>
    <td>tornado_virt_s1s2_native</td> <td>2</td> <td>624</td> <td>629</td> <td>620</td>
  </tr>
  <tr>
    <td>gevent_virt_s1s2</td> <td>2</td> <td>414</td> <td>417</td> <td>411</td>
  </tr>
  <tr>
    <td>gevent_virt_s1s2_alt</td> <td>2</td> <td>167</td> <td>171</td> <td>164</td>
  </tr>
  <tr>
    <td>tornado_virt_pypy</td> <td>2</td> <td>822</td> <td>855</td> <td>789</td>
  </tr>
</table>

The following table presents how "request/s" evolves as the client load increases.
The columns represent the number of parallel connections in the client that generates the load.

<table>
  <tr>
    <th>Test Case</th> <th>10</th> <th>20</th>  <th>30</th>  <th>40</th>  <th>50</th> 
  </tr>
  <tr>
    <td>tornado_inc_load</td> <td>896</td> <td>899</td> <td>879</td> <td>862</td> <td>852</td>
  </tr>
  <tr>
    <td>gevent_inc_load</td> <td>462</td> <td>446</td> <td>437</td> <td>308</td> <td>256</td>
  </tr>
  <tr>
    <td>gevent_inc_load_alt</td> <td>518</td> <td>508</td> <td>413</td> <td>310</td> <td>311</td>
  </tr>
</table> 

[The attached Benchmarks.md file](https://github.com/globocom/benchmark-python-wsgi/blob/master/Benchmarks.md) contains 
 dumps of the raw tests executed.


Conclusions
-----------

Tornado shows consistently a better performance than Gevent considering just "requests/s", and responds better when we
increase the number of requests, thus, it is a good hint that will scale better.
However, the code produced with Gevent was cleaner and more readable than the code produced with Tornado.

When using Tornado, the adoption of the pycurl client (instead of the [native client](http://www.tornadoweb.org/documentation/httpclient.html))
provides an enhancement in the performance.

The use of Flask significantly reduces the performance of both Tornado or Gevent.

Comparing *tornado_virt_s3* with *tornado_virt_pypy* showed that PyPy adoption did not contributed to any performance enhancement.
We were unable to run PyPy with Gevent. 

We did not have consistent results of which is the best http client for Gevent:
either the patched "requests" lib or "geventhttpclient".
When the servers are separate (more realistic use case),  patched "requests" performed better than "geventhttpclient".

We did some other tests accessing a backend Redis server, instead of Virtuoso.
The source code is also published in this project, but we did not reported here the detailed results of those tests.
When querying the Redis server using a synchronous driver the results of Tornado and Gevent had equivalent performances,
however neither was stable.

DISCLAIMER: This is a quick-and-dirty benchmark for us to have a glimpse of how to code in Tornado in comparison
            with how to code in Gevent, and to have a coarse grain idea of performance. A serious benchmark would
            need much more repetitions under more controlled conditions.


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

