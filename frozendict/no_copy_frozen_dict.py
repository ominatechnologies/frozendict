from __future__ import annotations

from typing import Mapping, TypeVar

from .frozen_dict import FrozenDict

KT = TypeVar("KT")
VT_co = TypeVar("VT_co", covariant=True)


class NoCopyFrozenDict(FrozenDict[KT, VT_co]):
    def __init__(self,
                 value: Mapping[KT, VT_co] = None,
                 *,
                 homogeneous_type: bool = False,
                 remove_none_values: bool = False,
                 no_copy: bool = True,
                 **kwargs):
        """
        Instantiate a FrozenDict without making a copy of the given dictionary.

        WARNING: By definition it is not immutable but will perform better.
        A good usage would be when you instantiate a frozendict inline.
        Ex: NoCopyFrozenDict({k1:v1, k2:v2}) is safe and immutable

        :param value: A mapping from which to create a FrozenDict.
        :param homogeneous_type: Option to check that all types in
            the dictionary are homogeneous, all keys should have the same
            type and all values should have the same type.
        :param remove_none_values: Option to remove all None value from the
            given mapping.
        :param no_copy: Option to enable the copy of the given mapping.
        :param kwargs: You can use kwargs to instantiate a FrozenDict.
            Ex: FrozenDict(k1:v1, k2:v2)
        """
        super().__init__(value,
                         homogeneous_type=homogeneous_type,
                         remove_none_values=remove_none_values,
                         no_copy=no_copy,
                         **kwargs)
