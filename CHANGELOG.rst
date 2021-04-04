Frozendict Changelog
====================
.. inclusion-marker

Head `refactor_21`
++++++++++++++++++
- Drop support for Python 3.7.


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
