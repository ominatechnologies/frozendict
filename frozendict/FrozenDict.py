from __future__ import annotations

from typing import TypeVar, Mapping, Dict, Optional

T = TypeVar('T')


class FrozenDict(Mapping[str, T]):
    __slots__ = ['_hash_cache', '_dict']

    _hash_cache: Optional[int]
    _dict: Mapping[str, T]

    def __init__(self, value: Mapping[str, T] = None, **kwargs):
        self._hash_cache = None

        def is_same_type(x) -> bool:
            if is_same_type.value_type:
                return x == is_same_type.value_type
            else:
                is_same_type.value_type = x
                return True

        is_same_type.value_type = None

        if value is not None:
            if not (isinstance(value, Mapping)
                    and isinstance(value, Dict)
                    and all(isinstance(k, str) and is_same_type(type(v))
                            for k, v in value.items())):
                raise ValueError()
            self._dict = value.copy()
        elif len(kwargs) > 0:
            if not all(isinstance(k, str) and is_same_type(type(v))
                       for k, v in kwargs.items()):
                raise ValueError()
            self._dict = dict(**kwargs)
        else:
            self._dict = dict()

    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __or__(self, other):
        if isinstance(other, dict):
            return FrozenDict(dict(self._dict, **other))
        elif isinstance(other, FrozenDict):
            return FrozenDict(dict(self._dict, **other._dict))
        else:
            return NotImplemented

    def union(self, other):
        return self.__or__(other)

    def __and__(self, other):
        if isinstance(other, dict):
            d = {k: v for k, v in self._dict.items() if k in other}
            return FrozenDict(d)
        elif isinstance(other, FrozenDict):
            d = {k: v for k, v in self._dict.items() if k in other._dict}
            return FrozenDict(d)
        else:
            return NotImplemented

    def intersection(self, other):
        return self.__and__(other)

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self._dict)

    def __hash__(self):
        if self._hash_cache is not None:
            return self._hash_cache
        rv = self._hash_cache = hash(frozenset(self._dict.items()))
        return rv


EMPTY_FROZEN_DICT: FrozenDict = FrozenDict()


def frozendict(value: Mapping[str, T] = None, **kwargs) -> FrozenDict[T]:
    if value is None and len(kwargs) == 0:
        return EMPTY_FROZEN_DICT
    else:
        return FrozenDict(value, **kwargs)
