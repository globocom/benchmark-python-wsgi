This is the procedure used to install all the necessary software stack for the tests.

Application setup
-----------------
   
    ssh ubuntu@ec2-54-234-130-164.compute-1.amazonaws.com -i ~/.ssh/benchmark_amazon.pem
    sudo apt-get update
    sudo apt-get install make git python-dev libevent-dev

Python
------
    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install virtualenv virtualenvwrapper
    source `which virtualenvwrapper.sh`

PyPy
-----
    sudo apt-get install pypy
    mkvirtualenv benchmark_pypy --python=pypy
    workon benchmark_pypy
    make install

Project Code
------------
    sudo apt-get install libcurl4-gnutls-dev librtmp-dev # pycurl dependencies
    mkvirtualenv benchmark
    git clone git://github.com/globocom/benchmark-python-wsgi.git
    cd benchmark-python-wsgi
    make install

Virtuoso
--------
    
    sudo apt-get install virtuoso-opensource
    # senha: dba (2 vezes)
    /usr/bin/isql-vt 1111 dba dba
    SPARQL CREATE GRAPH <http://graph-uri>  ;
    SPARQL INSERT DATA INTO <http://graph-uri> { <http://dummyClass.com> a owl:Class . <http://dummyObj.com> a <http://dummyClass.com> . }  ;
    

Redis
-----
    sudo apt-get install redis-server



Client-side setup
=================

    sudo apt-get update
    sudo apt-get install make gcc git

Install WRK
-----------

    git clone git://github.com/wg/wrk.git
    cd wrk
    make


Install weighttp
----------------

    sudo apt-get install libev-dev
    git clone git://git.lighttpd.net/weighttp
    cd weighttp
     ./waf configure
    ./waf build
    sudo ./waf install
