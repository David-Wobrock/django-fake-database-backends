=============================
Django fake database backends
=============================

.. image:: https://travis-ci.org/David-Wobrock/django-fake-database-backends.svg?branch=master
    :target: https://travis-ci.org/David-Wobrock/django-fake-database-backends

.. image:: https://img.shields.io/pypi/v/django-fake-database-backends.svg
    :target: https://pypi.python.org/pypi/django-fake-database-backends/

Motivations
-----------

This project intends to propose django database backends which can be used to generated SQL, without actually having the databases set up.
The main use case is using the built-in django command ``manage.py sqlmigrate``.

These backends are not intended to be used for any production, migration or storage.
They will nicely fail when you try to actually establish an actual database connection.

The need for this library comes from the tests of `django-migration-linter`_ which needed to generate SQL from a backend that was not sqlite3, but without having to install a database client library.

.. _`django-migration-linter`: https://github.com/3YOURMIND/django-migration-linter

Installation
------------

::

    pip install django-fake-database-backends

Usage
-----

In your project settings file, presumably ``settings.py``, use one of the available backends::

    DATABASES = {
        'default': {
            'ENGINE': 'django_fake_database_backends.backends.mysql',
        }
    }

Available backends
------------------

* ``django_fake_database_backends.backends.mysql``
* ``django_fake_database_backends.backends.sqlite3``

More will come in the future.

Tests
-----

The test suite uses `tox`_ and can be invoked using.

.. _`tox`: https://pypi.python.org/pypi/tox
