from typing import Dict, Mapping, Optional, Union

from pytest import raises

from frozendict import AbstractDict, FrozenDict, NoCopyFrozenDict, frozendict


def test_init_1():
    assert frozendict is FrozenDict

    fd: AbstractDict = FrozenDict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, AbstractDict)
    assert isinstance(fd, Mapping)


def test_init_3():
    fd: FrozenDict = FrozenDict({})
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, AbstractDict)
    assert isinstance(fd, Mapping)


def test_init_4():
    fd: FrozenDict[str, int] = FrozenDict({"k_1": 123})
    assert fd.get("k_1") == 123


def test_init_5():
    fd: FrozenDict[str, str] = FrozenDict({"k_1": "0"})
    assert fd.get("k_1") == "0"


def test_init_6():
    fd: FrozenDict[int, int] = FrozenDict({1: 0})
    assert fd.get(1) == 0


def test_init_7():
    fd: FrozenDict[str, Union[int, str]] = FrozenDict({"k_1": 0, "k_2": "v_2"})
    assert fd.get("k_1") == 0
    assert fd.get("k_2") == "v_2"


def test_init_8():
    with raises(TypeError):
        FrozenDict({"k_1": 0, "k_2": "v_2", "k_3": {"sk_1": 1, "sk_2": "2"}})


def test_init_non_dict():
    with raises(TypeError):
        # noinspection PyTypeChecker
        FrozenDict({"1", "0"})  # type: ignore

    with raises(TypeError):
        # noinspection PyTypeChecker
        FrozenDict({1, 0})  # type: ignore


def test_init_homogeneous():
    with raises(TypeError):
        FrozenDict({"k_1": 0, "k_2": "1"}, homogeneous_type=True)
    with raises(TypeError):
        FrozenDict(k_1=0, k_2="1", homogeneous_type=True)
    with raises(TypeError):
        FrozenDict({"k_1": 0, 1: 1}, homogeneous_type=True)
    with raises(TypeError):
        FrozenDict({"k_1": 0, 1: "1"}, homogeneous_type=True)


def test_init_kwargs_1():
    fd_1: FrozenDict[str, int]
    fd_1 = FrozenDict(k_1=0)
    assert fd_1.keys() == {"k_1"}
    assert fd_1.get("k_1") == 0

    fd_1 = FrozenDict(k_1=0, k_2=1)
    assert fd_1.keys() == {"k_1", "k_2"}
    assert fd_1.get("k_1") == 0
    assert fd_1.get("k_2") == 1

    fd_1 = FrozenDict(k_1=0, k_2=1)
    assert fd_1.keys() == {"k_1", "k_2"}
    assert fd_1.get("k_1") == 0
    assert fd_1.get("k_2") == 1

    fd_2: FrozenDict[str, Union[int, str]]
    fd_2 = FrozenDict(k_1=0, k_2="1")
    assert fd_2.keys() == {"k_1", "k_2"}
    assert fd_2.get("k_1") == 0
    assert fd_2.get("k_2") == "1"

    fd_3: FrozenDict[str, Dict[str, int]]
    fd_3 = FrozenDict(
        k_1=frozendict({"k_1": 0, "k_2": 1}), k_2=frozendict({"k_3": 2, "k_4": 3})
    )
    assert fd_3.keys() == {"k_1", "k_2"}
    assert fd_3.get("k_1") == {"k_1": 0, "k_2": 1}
    assert fd_3.get("k_2") == {"k_3": 2, "k_4": 3}

    with raises(TypeError):
        FrozenDict(k_1={"k_1": 0, "k_2": 1}, k_2={"k_3": 2, "k_4": 3})


def test_init_no_none_value():
    fd: FrozenDict[str, Optional[int]]
    fd = FrozenDict({"k_1": 0}, remove_none_values=True)
    assert len(fd) == 1
    assert fd.get("k_1") == 0

    fd = FrozenDict({"k_1": 0, "k_2": None}, remove_none_values=True)
    assert len(fd) == 1
    assert fd.get("k_1") == 0

    fd = FrozenDict(
        {"k_1": 0, "k_2": None}, remove_none_values=True, homogeneous_type=True
    )
    assert len(fd) == 1
    assert fd.get("k_1") == 0

    fd = FrozenDict(k_1=0, k_2=None, remove_none_values=True)
    assert len(fd) == 1
    assert fd.get("k_1") == 0

    fd = FrozenDict(k_1=0, k_2=None, remove_none_values=True, homogeneous_type=True)
    assert len(fd) == 1
    assert fd.get("k_1") == 0


def test_singleton():
    assert FrozenDict() is FrozenDict._empty_frozendict
    assert FrozenDict() is FrozenDict()
    assert FrozenDict() is FrozenDict({})
    assert FrozenDict({}) is FrozenDict()
    assert FrozenDict({}) is FrozenDict({})

    assert FrozenDict({"k_1": "test"}) is not FrozenDict()
    assert FrozenDict() is not FrozenDict({"k_1": "test"})
    assert FrozenDict() is not FrozenDict(k_1=0)
    assert FrozenDict({"k_1": "test"}) is not FrozenDict({"k_1": "test"})
    assert FrozenDict(k_1=0) is not FrozenDict({"k_1": "test"})
    assert FrozenDict(k_1=0) is not FrozenDict(k_1=0)


def test_equality():
    assert FrozenDict() == FrozenDict()
    assert FrozenDict({"k_1": 0}) == FrozenDict({"k_1": 0})
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd == d
    assert FrozenDict() != FrozenDict({"k_1": 0})
    assert FrozenDict({"k_1": 1}) != FrozenDict({"k_1": 0})
    assert FrozenDict({"k_2": 0}) != FrozenDict({"k_1": 0})
    assert FrozenDict(d) != {"k_1", "k_2"}


def test_hash_1():
    assert hash(FrozenDict()) == hash(FrozenDict())
    assert hash(FrozenDict({"k_1": 0})) == hash(FrozenDict({"k_1": 0}))
    d = {"k_1": 0, "k_2": 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert hash(fd) == hash(FrozenDict(d))
    assert hash(fd) == hash(fd)
    assert hash(FrozenDict()) != hash(FrozenDict({"k_1": 0}))
    assert hash(FrozenDict({"k_1": 1})) != hash(FrozenDict({"k_1": 0}))
    assert hash(FrozenDict({"k_2": 0})) != hash(FrozenDict({"k_1": 0}))


def test_hash_2():
    d_1 = {"k_1": 0, "k_2": 1}
    d_2 = {"k_3": d_1}
    with raises(TypeError):
        FrozenDict(d_2)


def test_immutable_1():
    fd: FrozenDict[str, int]
    d: Dict[str, int] = {"k_1": 0, "k_2": 1}

    fd = FrozenDict(d)
    assert fd.items() == d.items()
    d["test3"] = 3
    assert d.get("test3") == 3
    assert not fd.get("test3")

    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({"k_1": fd})
    assert ffd.get("k_1") == fd
    assert len({fd, fd, fd, fd, fd, fd}) == 1


def test_immutable_2():
    fd_1: FrozenDict[str, int] = frozendict({"k_1": 0, "k_2": 1})
    fd_2: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({"k_3": fd_1})
    assert fd_2.get("k_3").get("k_1") == 0  # type: ignore


def test_immutable_3():
    fd_1a: FrozenDict[str, int] = frozendict({"k_1": 0, "k_2": 1})
    fd_1b: FrozenDict[str, int] = frozendict({"k_1": 1})
    fd_2: FrozenDict[str, FrozenDict[str, int]] = FrozenDict(k_1=fd_1a, k_2=fd_1b)
    assert fd_2.get("k_1").get("k_1") == 0  # type: ignore


def test_immutable_no_copy():
    d = {"k_1": 0, "k_2": 1}
    fd_1: FrozenDict[str, int] = frozendict(d, no_copy=True)
    assert fd_1.items() == d.items()
    d["k_3"] = 3
    assert d.get("k_3") == 3
    assert fd_1.get("k_3") == 3


def test_immutable_no_copy_1():
    d: Dict[str, int] = {"k_1": 0, "k_2": 1}

    fd_2: FrozenDict[str, int] = NoCopyFrozenDict(d)
    assert isinstance(fd_2, NoCopyFrozenDict)
    assert isinstance(fd_2, FrozenDict)
    assert fd_2.items() == d.items()
    d["k_3"] = 3
    assert d.get("k_3") == 3
    assert fd_2.get("k_3") == 3

    fd_3: FrozenDict[str, Dict[str, int]] = NoCopyFrozenDict(k=fd_2)
    assert isinstance(fd_3, NoCopyFrozenDict)
    assert isinstance(fd_3, FrozenDict)
    assert d.get("k_3") == 3
    assert fd_3.get("k").get("k_3") == 3  # type: ignore


def test_typing_1():
    class ClassA:
        pass

    def f_1(dct: FrozenDict[str, Optional[ClassA]]):
        # f_2(dct["k_1"])
        return dct

    dct_1: FrozenDict[str, ClassA] = FrozenDict({"k_1": ClassA()})
    f_1(dct_1)


def test_typing_2():
    class ClassA:
        pass

    class ClassB(ClassA):
        pass

    def f_1(dct: FrozenDict[str, ClassB]):
        f_2(dct)

    def f_2(dct: FrozenDict[str, ClassA]):
        return dct

    f_1(FrozenDict({"k_1": ClassB()}))


def test_typing_3():
    class ClassA:
        pass

    def f_1(dct: FrozenDict[str, ClassA]):
        f_2(dct)

    def f_2(dct: FrozenDict[str, Optional[ClassA]]):
        return dct

    f_1(FrozenDict({"k_1": ClassA()}))
