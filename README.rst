========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-pyggui/badge/?style=flat
    :target: https://python-pyggui.readthedocs.io/
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/pyggui.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pyggui

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyggui.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pyggui

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyggui.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pyggui

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyggui.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pyggui

.. |commits-since| image:: https://img.shields.io/github/commits-since/15minutOdmora/python-pyggui/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/15minutOdmora/python-pyggui/compare/v0.0.0...main



.. end-badges

Pygame project for simplifying page and menu creation while still leaving full controll

* Free software: MIT license

Installation
============

::

    pip install pyggui

You can also install the in-development version with::

    pip install https://github.com/15minutOdmora/python-pyggui/archive/main.zip


Documentation
=============


https://python-pyggui.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
