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
linting.

This project uses sphinx_ to generate its documentation. To be able to build
the docs as latex/pdf, you need to install the proper tex tools.
On MacOS, install MacTex_ and latexmk_.

To install a virtual environment with all the necessary packages and tools use
the following command::

    $ make install

There are other commands in the makefile, to see them run::

    $ make help

NOTE: Do not forget to activate your virtual environment in your terminal.

You can run tests and tools with::

    $ (venv) pytest
    $ (venv) mypy frozendict
    $ (venv) flake8 frozendict tests
    $ (venv) pytest-watch
    $ (venv) coverage run -m pytest
    $ (venv) coverage report

We also use tox to test and produce documentation, you can check available
configured environment by running::

    $ tox -l

FYI:
    - local: it means that it use the version you have checkout locally
    - dev: it means that it will use the version from main
    - prod: it means that it will use the version given in the setup.py
    - test: it means that it will run pytest, mypy and flake8

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
