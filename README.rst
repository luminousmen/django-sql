.. image:: https://travis-ci.org/luminousmen/django-sql.svg?branch=master
    :target: https://travis-ci.org/luminousmen/django-sql

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/luminousmen/django-sql/blob/master/LICENCE


Django-SQL
====
A simple app for executing SQL queries in Django admin panel.

.. warning::

   Do not install this app if you afraid of consequences of giving access to database from admin panel.


============
Requirements
============

* Python3
* Django 1.9


============
Installation
============

.. code-block:: bash

    pip install git+https://github.com/luminousmen/django-sql.git


Add to your INSTALLED_APPS in settings.py:


.. code-block::

    INSTALLED_APPS = [
      ...
      'sql',
    ]


Add to your `urls.py`:


.. code-block::

    url(r'^admin/sql/(?:sql/)?$', execute_sql, name='sql'),
