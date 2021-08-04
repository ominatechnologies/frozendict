Frozendict Changelog
====================
.. inclusion-marker


Head
++++

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
