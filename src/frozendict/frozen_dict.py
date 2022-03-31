from __future__ import annotations

from gettext import gettext as _
from typing import (
    Any,
    ClassVar,
    Dict,
    Hashable,
    Iterator,
    Mapping,
    Optional,
    Set,
    TypeVar,
)

import xxhash

KT = TypeVar("KT")
VT_co = TypeVar("VT_co", covariant=True)

__OPTIONAL_KEYS__: Set[str] = {
    "homogeneous_type",
    "remove_none_values",
    "no_copy",
}


class FrozenDict(Mapping[KT, VT_co]):
    """An immutable dictionary that implements the "py:class:`~typing.Mapping`
    protocol and other :py:class:`~dict` methods.
    """

    # -- Class Initialization --------------- --- --  -

    _empty_frozendict: ClassVar[Optional[FrozenDict]] = None

    # -- Instance Initialization --------------- --- --  -

    __slots__ = ["_hash_cache", "_dict"]

    _hash_cache: Optional[int]
    _dict: Dict[KT, VT_co]

    def __new__(cls, *args, **kwargs):
        if (len(args) == 0 or args[0] is None or len(args[0]) == 0) and len(
            set(kwargs.keys()) - __OPTIONAL_KEYS__
        ) == 0:
            # Return the same empty frozendict:
            if cls._empty_frozendict is None:
                cls._empty_frozendict = super(FrozenDict, cls).__new__(cls)
            return cls._empty_frozendict
        elif len(args) == 1 and isinstance(args[0], FrozenDict):
            # Return the given FrozenDict as is:
            return args[0]
        else:
            # Initialize a new FrozenDict.
            return super().__new__(cls)

    def __getnewargs__(self):
        # When instantiating a frozendict object, the static `__new__` method
        # is called with the arguments passed to the constructor. When the
        # `args` argument is "empty" then the "empty" frozendict singleton in
        # returned.
        #
        # However, when unpickling a class instance, the static `__new__`
        # method is called without arguments to instantiate a "fresh" instance.
        # The unpickling process then updates the `__dct__` with the unpickled
        # properties. Because of this, the `__new__` method cannot distinguish
        # between "regular" instantiations of "empty" frozen dictionaries and
        # "empty" instantiations as part of unpickling non-empty frozen
        # dictionaries. Hence it cannot decide when to yield the "empty"
        # frozendict singleton and when not to.
        #
        # The `__getnewargs__` implementation is provided to remedy this
        # problem. When unpickling an object, this method is called and the
        # result is passed to the `__new__` method as the `args` argument.
        # By returning a non-empty tuple of arguments for non-empty dicts,
        # the `__new__` method is capable of distinguishing between "regular"
        # instantiations of "empty" frozen dictionaries and "empty"
        # instantiations as part of unpickling non-empty frozen dictionaries.
        # Note that the actual argument returned by this method does not
        # matter, it just needs a non-empty tuple.
        #
        # Inspired by: https://github.com/Technologicat/unpythonic/issues/55
        if self is not self._empty_frozendict:
            # noinspection PyRedundantParentheses
            return ("non_empty",)
        return ()

    def __init__(
        self,
        value: Mapping[KT, VT_co] = None,
        *,
        homogeneous_type: bool = False,
        remove_none_values: bool = False,
        no_copy: bool = False,
        **kwargs,
    ):
        """Instantiate a FrozenDict.

        :param value: A mapping from which to create a FrozenDict.
        :param homogeneous_type: Option to check that all types in
            the dictionary are homogeneous, all keys should have the same
            type and all values should have the same type.
        :param remove_none_values: Option to remove any None value from the
            given mapping.
        :param no_copy: Option to disable the copy of the given mapping.
            Ex: frozendict({k1:v1, k2:v2}, no_copy=True) will create a safe
            and immutable object without copying as there are no references
            of the given value.
        :param kwargs: You can use kwargs to instantiate a FrozenDict.
            Ex: FrozenDict(k1:v1, k2:v2)
        """
        self._hash_cache = None

        def has_homogeneous_type(i) -> bool:
            """Check that the iterator contains only the same type."""
            iterator: Iterator[Any] = iter(i)
            first_type: Any = type(next(iterator, None))
            return all(type(x) is first_type for x in iterator)

        if value is not None:
            if not isinstance(value, Dict):
                if isinstance(value, Mapping):
                    value = dict(value)
                else:
                    msg = _("Expected a mapping as value, got a {}.")
                    raise TypeError(msg.format(type(value)))

            # The given value should be hashable
            for key, val in value.items():
                if not isinstance(key, Hashable):
                    msg = _("The key '{}' (of type: {}) is not hashable.")
                    raise TypeError(msg.format(key, type(key).__name__))
                if not isinstance(val, Hashable):
                    msg = _("The value for key '{}' (of type: {}) is not hashable.")
                    raise TypeError(msg.format(key, type(val).__name__))

            if remove_none_values:
                value = {k: v for k, v in value.items() if v is not None}
            if homogeneous_type and not (
                has_homogeneous_type(value.keys())
                and has_homogeneous_type(value.values())
            ):
                raise TypeError()
            if no_copy:
                self._dict = value
            else:
                self._dict = value.copy()
        elif len(kwargs) > 0:
            # The given kwargs should be hashable
            assert isinstance(hash(tuple(sorted(kwargs.items()))), int)

            buildable_kwargs = {
                k: v for k, v in kwargs.items() if k not in __OPTIONAL_KEYS__
            }
            if remove_none_values:
                buildable_kwargs = {
                    k: v for k, v in buildable_kwargs.items() if v is not None
                }
            if homogeneous_type and (
                not has_homogeneous_type(buildable_kwargs.keys())
                or not has_homogeneous_type(buildable_kwargs.values())
            ):
                raise TypeError
            self._dict = dict(**buildable_kwargs)  # type: ignore
        elif not hasattr(self, "_dict"):
            self._dict = {}

    # -- Dict Methods --------------- --- --  -

    def copy(self):
        """Returns the immutable dictionary."""
        return self

    def items(self):
        """Returns a copy of the dictionary’s list of (key, value) pairs."""
        return self._dict.items()

    def keys(self):
        """Returns a copy of the dictionary’s list of keys."""
        return self._dict.keys()

    def update(self, mapping: Mapping) -> FrozenDict:
        """Returns a new immutable dict that contains the key:value elements
        from this dict, updated with the key:value elements from the given
        mapping.

        Note that this method is not compatible with the `dict.update` method,
        which updates the dictionary in-place (destructively), while this
        method is non-destructive.

        :param mapping: Required. Either another dictionary object or an
            iterable of key:value pairs (iterables of length two). If keyword
            arguments are specified, the dictionary is then updated with those
            key:value pairs.
        :return: The new frozen dictionary.

        TODO: Should `homogeneous_type` or `remove_none_values` be supported ?
        """
        updated = self._dict.copy()
        updated.update(mapping)
        return FrozenDict(updated)

    def values(self):
        """Returns a copy of the dictionary’s list of values."""
        return self._dict.values()

    # -- Custom Methods --------------- --- --  -

    def intersection(self, other):
        """Returns the intersection of the given dictionaries. Equivalent to
        `self & other`."""
        return self.__and__(other)

    def serialize(self) -> Mapping:
        """Serialize the object to a form that can be passed to the
        :func:`json.dumps` function."""
        return {
            str(k): (v.serialize() if getattr(v, "serialize", None) else v)
            for k, v in self.items()
        }

    def union(self, other):
        """Returns the union of the given dictionaries. Equivalent to
        `self | other`."""
        return self.__or__(other)

    # -- Magic Methods --------------- --- --  -

    def __and__(self, other):
        if isinstance(other, Dict):
            d = {k: v for k, v in self._dict.items() if k in other}
            return FrozenDict(d)
        elif isinstance(other, FrozenDict):
            d = {k: v for k, v in self._dict.items() if k in other._dict}
            return FrozenDict(d)
        else:
            raise NotImplementedError()

    def __contains__(self, key):
        return key in self._dict

    def __copy__(self):
        return self

    def __deepcopy__(self, memo=None):
        return self

    def __eq__(self, other):
        if isinstance(other, FrozenDict):
            return self._dict == other._dict
        elif isinstance(other, Dict):
            return self._dict == other
        else:
            return False

    def __getitem__(self, key):
        return self._dict[key]

    def __hash__(self):
        if self._hash_cache is None:
            try:
                items = str(tuple(sorted(self._dict.items())))
            except TypeError:
                items = str(tuple(self._dict.items()))

            self._hash_cache = xxhash.xxh64(items, seed=0).intdigest()

        return self._hash_cache

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __or__(self, other):
        if isinstance(other, FrozenDict):
            return FrozenDict(dict(self._dict, **other._dict))
        elif isinstance(other, Dict):
            return FrozenDict(dict(self._dict, **other))
        else:
            raise NotImplementedError()

    def __repr__(self):
        return self._dict.__repr__()

    def __str__(self):
        return self._dict.__str__()


frozendict = FrozenDict
