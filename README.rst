Django-SQL
====
A simple app for executing SQL queries in Django admin

============
Requirements
============

* Python3


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
