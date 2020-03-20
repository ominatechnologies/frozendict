from __future__ import annotations

from typing import TypeVar, Mapping, Dict, Optional, Iterator, Any

T = TypeVar('T')
S = TypeVar('S')


class FrozenDict(Mapping[S, T]):
    __slots__ = ['_hash_cache', '_dict']

    _hash_cache: Optional[int]
    _dict: Mapping[S, T]

    def __init__(self,
                 value: Mapping[S, T] = None,
                 *,
                 homogeneous_type=False,
                 remove_none_value=False,
                 **kwargs):
        self._hash_cache = None

        def has_homogeneous_type(i) -> bool:
            iterator: Iterator[Any] = iter(i)
            first_type: Any = type(next(iterator, None))
            return all(type(x) is first_type for x in iterator)

        if value is not None:
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
            if remove_none_value:
                kwargs = {k: v for k, v in kwargs.items() if v is not None}
            if homogeneous_type and not has_homogeneous_type(kwargs.values()):
                raise TypeError
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


EMPTY_FROZEN_DICT: FrozenDict = FrozenDict()


def frozendict(value: Mapping[S, T] = None,
               *,
               homogeneous_type=False,
               remove_none_value=False,
               **kwargs) -> FrozenDict[S, T]:
    if value is None and len(kwargs) == 0:
        return EMPTY_FROZEN_DICT
    else:
        return FrozenDict(value,
                          homogeneous_type=homogeneous_type,
                          remove_none_value=remove_none_value,
                          **kwargs)
