from __future__ import annotations

from typing import Any, Dict, Iterator, Mapping, Optional, TypeVar

T = TypeVar('T')
S = TypeVar('S')


class FrozenDict(Mapping[S, T]):
    """
    An immutable dictionary that implements :py:class:`typing.Mapping`
    protocol for python 3.
    """
    __slots__ = ['_hash_cache', '_dict']

    _hash_cache: Optional[int]
    _dict: Mapping[S, T]
    _instance = None
    _optional_keys = {'homogeneous_type', 'remove_none_value'}

    def __new__(cls, *args, **kwargs):
        """
        Return a singleton instance if args and kwargs are empty
        """
        if ((len(args) == 0 or args[0] is None or len(args[0]) == 0)
                and len(set(kwargs.keys()) - cls._optional_keys) == 0):
            if cls._instance is None:
                cls._instance = super(FrozenDict, cls).__new__(cls)
            return cls._instance
        return super(FrozenDict, cls).__new__(cls)

    def __init__(self,
                 value: Mapping[S, T] = None,
                 *,
                 homogeneous_type=False,
                 remove_none_value=False,
                 **kwargs):
        self._hash_cache = None

        def has_homogeneous_type(i) -> bool:
            """
            Check that the iterator contains only the same type
            """
            iterator: Iterator[Any] = iter(i)
            first_type: Any = type(next(iterator, None))
            return all(type(x) is first_type for x in iterator)

        if value:
            if not isinstance(value, Mapping) or not isinstance(value, Dict):
                raise TypeError
            if remove_none_value:
                value = {k: v for k, v in value.items()
                         if v is not None}
            if homogeneous_type:
                if not (has_homogeneous_type(value.keys())
                        and has_homogeneous_type(value.values())):
                    raise TypeError
            self._dict = value.copy()
        elif len(kwargs) > 0:
            buildable_kwargs = {k: v for k, v in kwargs.items()
                                if k not in self._optional_keys}
            if remove_none_value:
                buildable_kwargs = {k: v for k, v in buildable_kwargs.items()
                                    if v is not None}
            if (homogeneous_type
                    and (not has_homogeneous_type(buildable_kwargs.keys())
                         or not has_homogeneous_type(
                                buildable_kwargs.values()))):
                raise TypeError
            self._dict = dict(**buildable_kwargs)
        else:
            self._dict = dict()

    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __or__(self, other):
        if isinstance(other, Dict):
            return FrozenDict(dict(self._dict, **other))
        elif isinstance(other, FrozenDict):
            return FrozenDict(dict(self._dict, **other._dict))
        else:
            raise NotImplementedError

    def union(self, other) -> FrozenDict[S, T]:
        return self.__or__(other)

    def __and__(self, other):
        if isinstance(other, Dict):
            d = {k: v for k, v in self._dict.items() if k in other}
            return FrozenDict(d)
        elif isinstance(other, FrozenDict):
            d = {k: v for k, v in self._dict.items() if k in other._dict}
            return FrozenDict(d)
        else:
            raise NotImplementedError

    def intersection(self, other) -> FrozenDict[S, T]:
        return self.__and__(other)

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self._dict)

    def __hash__(self):
        if self._hash_cache is not None:
            return self._hash_cache
        rv = self._hash_cache = hash(frozenset(self._dict.items()))
        return rv


def frozendict(value: Mapping[S, T] = None,
               *,
               homogeneous_type=False,
               remove_none_value=False,
               **kwargs) -> FrozenDict[S, T]:
    """
    Lowercase alias for the FrozenDict constructor
    :param value: a mutable dict to froze
    :param homogeneous_type: check that the content of the dictionary has
    homogeneous types for key and value.
    :param remove_none_value: remove any None value from the dictionary
    :param kwargs: It is possible to create the instance through kwargs
    :return:
    """
    return FrozenDict(value,
                      homogeneous_type=homogeneous_type,
                      remove_none_value=remove_none_value,
                      **kwargs)
