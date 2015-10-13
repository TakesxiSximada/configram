configram - pyramid style general propose configurator for non web application
==============================================================================

**configram** is a Python library which provides general propose configurator for non web application,
set the application in the same way as the configurator of pyramid.

It can read settings on the components of under hierarchy  by using **config.include()**. Settings is
usually be written in **includeme()** function. It will scan settings of application by calling **config.include**
to **includeme** of components of under hierarchy. **Configurator** will special treatment to **include()** and
**scan()** function. Other methods access will delegate to the Configurator held by itself. It is possible
to customize the behavior of that for Configurator.

Install
-------

::

   $ pip install configram

How to use it
-------------

case - simple non web application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with Celery (redis backend)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with Celery (rabbitmq backend)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with zmq(ZeroMQ)
^^^^^^^^^^^^^^^^^^^^^^^

case - with scrapy
^^^^^^^^^^^^^^^^^^

case - with Luigi
^^^^^^^^^^^^^^^^^

case - with Tornado
^^^^^^^^^^^^^^^^^^^

case - with Pyramid
^^^^^^^^^^^^^^^^^^^

case - with Django
^^^^^^^^^^^^^^^^^^

case - with Flask
^^^^^^^^^^^^^^^^^^

case - with Bottle
^^^^^^^^^^^^^^^^^^

case - with Twisted
^^^^^^^^^^^^^^^^^^^

case - with pylons
^^^^^^^^^^^^^^^^^^

case - with SQLAlchemy(MySQL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with SQLAlchemy(PostgreSQL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with SQLAlchemy(SQLite3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with PyMySQL
^^^^^^^^^^^^^^^^^^^

case - with psycopg (PostgreSQL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with Aerospike
^^^^^^^^^^^^^^^^^^^^^

case - with Redis
^^^^^^^^^^^^^^^^^

case - with Mongo
^^^^^^^^^^^^^^^^^

case - with Pika(RabbitMQ)
^^^^^^^^^^^^^^^^^^^^^^^^^^

case - with AWS SQS
^^^^^^^^^^^^^^^^^^^

case - with AWS SNS
^^^^^^^^^^^^^^^^^^^

case - with AWS SES
^^^^^^^^^^^^^^^^^^^

case - with Heroku
^^^^^^^^^^^^^^^^^^

case - with Bluemix
^^^^^^^^^^^^^^^^^^^

case - with Google App Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
