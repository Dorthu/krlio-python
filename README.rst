krl.io python
=============

The *official* python library for `krl.io`_

Installation
------------
::

    pip install krlio

Building from Source
--------------------

To build and install this package:

- Clone us `on github`_
- ``./setup.py install``

Usage
-----
::

    import krlio

    url = krlio.get_link(shortcode)

    shortlink = krlio.make_anon_link(url)

.. _krl.io: http://krl.io
.. _on github: https://github.com/dorthu/krlio-python
