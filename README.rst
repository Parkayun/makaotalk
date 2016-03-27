makaotalk
=========

.. image:: https://secure.travis-ci.org/Parkayun/makaotalk.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/makaotalk

.. image:: https://readthedocs.org/projects/makaotalk/badge/?version=latest
   :target: http://makaotalk.readthedocs.org/en/latest/
   :alt: :Documentation Status

makaotalk is a simple web based chat service.


Core Dependency
---------------

- flask

  - wsgi server

- gevent

  - real-time chat (socketio)


Quick Start
-----------

1. clone this project

.. sourcecode:: bash

   ~ $ git clone https://github.com/Parkayun/makaotalk.git

2. install dependencies

.. sourcecode:: bash

   ~ $ pip install -r requirements/dev.txt

3. set up db

.. sourcecode:: bash

   ~ $ export DB_PATH=sqlite:///../database.db
   ~ $ python manage.py setup_db

4. run server

.. sourcecode:: bash

   ~ $ python manage.py run

5. Tada!

.. sourcecode:: bash

   ~ $ open http://localhost:5000


Features
--------

- Create real-time chat room.
- Delete my chat message.
- Modify my chat message.


Code Convention
---------------

- Basically, It keeps PEP8.
- It keeps 119 columns.
