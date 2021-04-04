FrozenDict Readme
=================

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. inclusion-marker

This library provides a modern implementation of frozendict.

`API-Docs <https://ominatechnologies.github.io/frozendict/>`_

Project Setup
-------------
This project requires Python 3.8 or higher. It is supported for Python 3.8
and 3.9.

This project uses pytest_ as testing framework and our code provides type
hinting (see PEP-484_ and PEP-561_) to enable static type checking using mypy_.
For test-driven development, we use pytest-watch_. We use flake8_ for code
linting. Linting and static type checking are integrated in the standard
pytest_-managed testing.

This project uses sphinx_ to generate its documentation. To be able to build
the docs as latex/pdf, you need to install the proper tex tools.
On MacOS, install MacTex_ and latexmk_.

To install the package for normal use in your application, use::

    $ pip install .

To run the tests, use::

    $ pip install -r requirements.dev.txt
    $ pip install --editable .
    $ python3 -m pytest

or::

    $ tox -e pytest-dev-py38

For test-driven development, use::

    $ pip install -r requirements.dev.txt
    $ pip install --editable .
    $ pytest-watch

To enforce code formatting, install the git hook::

    $ flake8 --install-hook git
    $ git config --bool flake8.strict true

To build the docs as html, use::

    $ tox -e pytest-html

To build the docs as pdf, use::

    $ tox -e pytest-pdf

Pytest, mypy and flake8 are configured in the *setup.cfg* file. Sphinx and
its plugins are configured in *docs/conf.py*.


.. _flake8: http://flake8.pycqa.org
.. _latexmk: https://mg.readthedocs.io/latexmk.html
.. _MacTex: http://www.tug.org/mactex/mactex-download.html
.. _mypy: http://mypy-lang.org
.. _PEP-484: https://www.python.org/dev/peps/pep-0484
.. _PEP-561: https://www.python.org/dev/peps/pep-0561
.. _pytest: https://docs.pytest.org
.. _pytest-watch: https://github.com/joeyespo/pytest-watch
.. _setuptools: https://setuptools.readthedocs.io
.. _sphinx: http://www.sphinx-doc.org
