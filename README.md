[![.github/workflows/tag.yml](https://github.com/ominatechnologies/frozendict/actions/workflows/tag.yml/badge.svg)](https://github.com/ominatechnologies/frozendict/actions/workflows/tag.yml)

# FrozenDict

This library provides a modern implementation of frozendict.

Check the doc here: [API-Docs](https://ominatechnologies.github.io/frozendict/)

## Project Setup

This project requires Python 3.8 or higher. It is supported for Python 3.8
and 3.9.

This project uses [pytest](https://docs.pytest.org) as testing framework and our code provides type
hinting (see [PEP-484](https://www.python.org/dev/peps/pep-0484) and [PEP-561](https://www.python.org/dev/peps/pep-0561)) to enable static type checking using [mypy](http://mypy-lang.org).
For test-driven development, we use [pytest-watch](https://github.com/joeyespo/pytest-watch). We use [flake8](http://flake8.pycqa.org) for code
linting.

This project uses [sphinx](http://www.sphinx-doc.org) to generate its documentation. To be able to build
the docs as latex/pdf, you need to install the proper tex tools.
On MacOS, install [MacTex](http://www.tug.org/mactex/mactex-download.html) and [latexmk](https://mg.readthedocs.io/latexmk.html).

To install a virtual environment with all the necessary packages and tools use
the following command:

    $ make install

There are other commands in the makefile, to see them run:

    $ make help

> **NOTE**: Do not forget to activate your virtual environment in your terminal.

Example:

    $ source venv/bin/activate

You can run tests and tools with:

    $ (venv) pytest
    $ (venv) mypy frozendict tests
    $ (venv) flake8
    $ (venv) pytest-watch
    $ (venv) coverage run -m pytest
    $ (venv) coverage report

We also use tox to test and produce documentation, you can check available
configured environment by running:

    $ tox -l

You can then run the selected environment with:

    $ tox -e selected_environment

Pytest, mypy and flake8 are configured in the *setup.cfg* file.
Sphinx and its plugins are configured in *docs/conf.py*.
