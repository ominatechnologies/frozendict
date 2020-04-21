# test_no_copy_frozen_dict

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from frozendict import NoCopyFrozenDict


@dataclass()
class Foo:
    fd: NoCopyFrozenDict[str, float]


def test_typing_1():
    dct: Dict[str, float] = {'k_1': 1.0}
    fd: NoCopyFrozenDict[str, float] = NoCopyFrozenDict(dct)
    assert fd == dct


def test_typing_2():
    dct: Dict[str, float] = {'k_1': 1.0}

    def check(fd: NoCopyFrozenDict[str, float]):
        assert fd == dct

    check(NoCopyFrozenDict(dct))


def test_typing_3():
    dct: Dict[str, float] = {'k_1': 1.0}
    foo = Foo(fd=NoCopyFrozenDict(dct))
    assert foo.fd == dct


def test_repr():
    # We want "<FrozenDict ...>" instead of "<NoCopyFrozenDict ...>"
    dct = NoCopyFrozenDict({"k_1": 1.0})
    assert repr(dct) == "<FrozenDict {'k_1': 1.0}>"
