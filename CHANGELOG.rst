Changelog
=========
.. inclusion-marker

v1.0 - 2020-04-15
+++++++++++++++++
- Initial implementation of the 'FrozenDict' class.
- Added 'AbstractDict' as alias of 'Mapping'.


v1.1 - 2020-04-13
+++++++++++++++++
- Add 'serialize' method.


v1.2 - 2020-04-15
+++++++++++++++++
- Add the 'no_copy' parameter to control whether the given dictionary is copied
  in the 'FrozenDict' constructor, which is False by default.
- Add the 'NoCopyFrozenDict' class for which the 'no_copy' parameter is True
  by default and which can be imported as a drop-in replacement using:
  :code:`from frozendict import NoCopyFrozenDict as FrozenDict`.
- Various fixes.
