FrozenDict Readme
=================

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status
.. image:: https://github.com/ominatechnologies/frozendict/workflows/Test%20package/badge.svg
    :alt: Tests Status

.. inclusion-marker

This library provides a modern implementation of frozendict.

`API-Docs <https://ominatechnologies.github.io/frozendict/>`_

Project Setup
-------------
We use pytest_ as testing framework and our code provides type hinting (see
PEP-484_ and PEP-561_) to enable static type checking using mypy_. For
test-driven development, we use pytest-watch_. We use flake8_ for code
linting. Linting and static type checking are integrated in the standard
pytest_-managed testing.

This project uses sphinx_ to generate its documentation. To be able to build
the docs as latex/pdf, you need to install the proper tex tools.
On MacOS, install MacTex_ and latexmk_.

To install the package for normal use in your application, use::

    $ pip install .

To install the package for development, use::

    $ pip install -r requirements.txt
    $ pip install --editable . | { grep -v "already satisfied" || :; }

To run the tests, use::

    $ python -m pytest

For test-driven development, use::

    $ pytest-watch

To enforce code formatting, install the git hook::

    $ flake8 --install-hook git
    $ git config --bool flake8.strict true

To build the docs as html, use::

    $ sphinx-build -b html docs build

Pytest, mypy and flake8 are configured in the *setup.cfg* file. Sphinx and
its plugins are configured in *docs/conf.py*.

Roadmap
-------
See `<TODO.rst>`_.


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
