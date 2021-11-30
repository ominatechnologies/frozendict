from typing import Mapping

from pytest import raises

from frozendict import FrozenDict


def test_len():
    fd1: FrozenDict = FrozenDict()
    assert len(fd1) == 0

    fd2: FrozenDict[str, int] = FrozenDict({"k_1": 0})
    assert len(fd2) == 1

    fd3: FrozenDict[str, int] = FrozenDict({"k_1": 0, "k_2": 1})
    assert len(fd3) == 2


def test_copy():
    fd_1 = FrozenDict({"k_1": 1, "k_2": 2})
    assert fd_1.copy() is fd_1


def test_get():
    fd: FrozenDict[str, int] = FrozenDict({"k_1": 0})
    assert fd.get("k_1") == 0
    assert fd.get("k_2") is None
    assert fd.get("k_2", 123) == 123


def test_items():
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd.items() == d.items()


def test_keys():
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd.keys() == d.keys()


def test_update():
    d_1 = {"k_1": 1, "k_2": 2}
    d_2 = {"k_2": 20, "k_3": 3}
    d_1.update(d_2)
    assert d_1 == {"k_1": 1, "k_2": 20, "k_3": 3}

    fd_1 = FrozenDict({"k_1": 1, "k_2": 2})
    fd_2 = FrozenDict({"k_2": 20, "k_3": 3})
    assert fd_1.update(fd_2) == FrozenDict({"k_1": 1, "k_2": 20, "k_3": 3})


def test_values():
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert list(fd.values()) == list(d.values())


def test_intersection():
    d1 = {"k_1": 0, "k_2": 1}
    d2 = {"k_1": 0, "k_3": 2}
    assert FrozenDict(d1) & FrozenDict(d2) == {"k_1": 0}
    assert FrozenDict(d1) & d2 == {"k_1": 0}
    assert FrozenDict(d1).intersection(FrozenDict(d2)) == {"k_1": 0}
    assert FrozenDict(d1).intersection(d2) == {"k_1": 0}

    with raises(NotImplementedError):
        FrozenDict() & ("k_1", 0)
    with raises(NotImplementedError):
        FrozenDict().intersection(("k_1", 0))


def test_union():
    d = {"k_1": 0, "k_2": 1}
    assert FrozenDict({"k_1": 0}) | FrozenDict({"k_2": 1}) == d
    assert FrozenDict({"k_1": 0}) | {"k_2": 1} == d
    assert FrozenDict({"k_1": 0}).union(FrozenDict({"k_2": 1})) == d
    assert FrozenDict({"k_1": 0}).union({"k_2": 1}) == d

    with raises(NotImplementedError):
        FrozenDict() | ("k_1", 0)
    with raises(NotImplementedError):
        FrozenDict().union(("k_1", 0))


def test_repr():
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({"k_1": fd})
    assert fd.__repr__() == "{'k_1': 0, 'k_2': 1}"
    assert ffd.__repr__() == "{'k_1': {'k_1': 0, 'k_2': 1}}"


def test_serialize():
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({"k_1": fd})
    s_fd: Mapping[str, int] = fd.serialize()
    s_ffd: Mapping[str, Mapping[str, int]] = ffd.serialize()
    assert s_fd == d
    assert s_ffd == {"k_1": d}
