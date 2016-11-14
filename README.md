[![Build Status](https://travis-ci.org/luminousmen/django-sql.svg?branch=master)](https://travis-ci.org/luminousmen/django-sql)
[![Coverage Status](https://coveralls.io/repos/github/luminousmen/django-sql/badge.svg?branch=master)](https://coveralls.io/github/luminousmen/django-sql?branch=master)
[![PyPI version](https://badge.fury.io/py/django-sql.svg)](https://badge.fury.io/py/django-sql)
[![Licence](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/luminousmen/django-sql/blob/master/LICENCE)


Django-SQL
====
A simple app for executing SQL queries in Django admin panel.

*! WARNINIG !*

   _Do not install this app if you afraid of consequences of giving access to database from admin panel._


##### Requirements

* Python3
* Django 1.9


##### Installation

```
    pip install django-sql
```

Add to your `INSTALLED_APPS` in `settings.py`:


```
    INSTALLED_APPS = [
      ...
      'sqlapp',
    ]
```

Add to your `urls.py`:


```
    url(r'^admin/sqlapp/(?:sql/)?$', execute_sql, name='sql'),
```

##### Contributors

* [luminousmen](https://github.com/luminousmen)
* [un-def](https://github.com/un-def)
