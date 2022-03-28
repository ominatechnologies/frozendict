Frozendict Changelog
====================
.. inclusion-marker

Head
++++

2022.3.28
+++++++++
- build: minor updates

2022.3.10
+++++++++
- Add: pre-commit auto update action
- build: Upgrade with refactored actions

2022.2.24
+++++++++
- Add: codeowners file

2022.2.14
+++++++++
- build: support for python 3.10
- build: Add auto bump signal to jai_lib

2022.1.27
+++++++++
- build: update editorconfig
- build: Run `pre-commit` on all files in the `test-py38` environment.

2022.1.25
+++++++++
- build: Add black
- build: Add the EditorConfig file.

2022.1.6
++++++++
- build: fix packaging

2022.1.4
++++++++
- build: fix packaging

2021.11.30
++++++++++
- build: add flake8-quotes to pre-commit

2021.11.26
++++++++++
- chore: update requirements

2021.11.10.1
++++++++++++
- fix: bumpver
- fix: caching for pre-commit.

2021.11.9
+++++++++
- feat: tagging in CI with branch protection rules

2021.11.8
+++++++++
- fix: The pytest-watch extensions should be listed on one line.

2021.11.5
+++++++++
- fix: tagging CI

2021.11.4
+++++++++
- fix: CI python cache

2021.10.29
++++++++++
- feat: Add i18n for error strings.

2021.9.29
+++++++++
- build: add pre-commit check on the CI (#13)

2021.9.28
+++++++++
- fix: prevent tagging failure from merging not rebased branch

2021.9.27.3
+++++++++++
- build: update flake8 config for .eggs

2021.9.27.2
+++++++++++
- build: update CI with linting and type checking

2021.9.27.1
+++++++++++
- build: update flake8 config

2021.9.27
+++++++++
- build: update readme

2021.9.16
+++++++++
- build: update pipelines with pip cache

2021.9.11
+++++++++
- fix: Drop stale environment variables.

2021.9.10
+++++++++
- build: update tox (alphabetically ordering)

2021.9.8
++++++++
- build: Update tox

2021.9.1.2
++++++++++
- chore: move typing-extensions to dev requirements

2021.9.1.1
++++++++++
- build: fix auto tagging

2021.9.1
++++++++
- fix: auto tagging

2021.08.04
++++++++++
- feat: Add the `update(mapping)` method.
- doc: Add documentation.


2021.07.22
++++++++++
- refactor: Drop (explicit) support for Python 3.7.
- fix: Various minor updates.
- fix: Reverse the change logs order.
- test: Provide a new/updated set of test commands that use tox-based test
  environments.
- chore: Update dependencies.


2021.5.17
+++++++++
- chore: Update dependencies.


2021.4.14
+++++++++
- refactor: Drop support for Python 3.7.
- fix: Minor updates.
- chore: Update dependencies.


2021.01.07
++++++++++
- fix: Minor updates.


2020.12.29
++++++++++
- chore: Update dependencies.


2020.12.16
++++++++++
- test: Add a separate type checking tox env that produces more intelligible
  error information compared to when using the pytest-mypy plugin.
- chore: Update dependencies.


2020.11.25
++++++++++
- fix: Support Python 3.9.
- fix: Various improvements and fixes.
- chore: Update dependencies.


2020.10.14
++++++++++
- fix: Various minor improvements and fixes.
- chore: Update dependencies.


v1.2 - 2020-04-15
+++++++++++++++++
- Add the 'no_copy' parameter to control whether the given dictionary is copied
  in the 'FrozenDict' constructor, which is False by default.
- Add the 'NoCopyFrozenDict' class for which the 'no_copy' parameter is True
  by default and which can be imported as a drop-in replacement using:
  :code:`from frozendict import NoCopyFrozenDict as FrozenDict`.
- Various fixes.


v1.1 - 2020-04-13
+++++++++++++++++
- Add 'serialize' method.


v1.0 - 2020-04-15
+++++++++++++++++
- Initial implementation of the 'FrozenDict' class.
- Added 'AbstractDict' as alias of 'Mapping'.
