Frozendict Changelog
====================
.. inclusion-marker

Head
++++

2021.11.10
++++++++++
- fix: caching for pre-commit.

2021.11.9
+++++++++
- feature: tagging in CI with branch protection rules

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
- infra: add pre-commit check on the CI (#13)

2021.9.28
+++++++++
- fix: prevent tagging failure from merging not rebased branch

2021.9.27.3
+++++++++++
- infra: update flake8 config for .eggs

2021.9.27.2
+++++++++++
- infra: update CI with linting and type checking

2021.9.27.1
+++++++++++
- infra: update flake8 config

2021.9.27
+++++++++
- infra: update readme

2021.9.16
+++++++++
- infra: update pipelines with pip cache

2021.9.11
+++++++++
- fix: Drop stale environment variables.

2021.9.10
+++++++++
- infra: update tox (alphabetically ordering)

2021.9.8
++++++++
- infra: Update tox

2021.9.1.2
++++++++++
- chore: move typing-extensions to dev requirements

2021.9.1.1
++++++++++
- infra: fix auto tagging

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
