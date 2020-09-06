# test_pickling

import pickle

from frozendict import FrozenDict, NoCopyFrozenDict  # noqa: F401


def test_1():
    fd_1 = FrozenDict({"k_1": "v_1"})
    fd_2 = pickle.loads(pickle.dumps(fd_1))
    assert set(fd_2.keys()) == {"k_1"}
    assert fd_2["k_1"] == "v_1"


def test_2():
    fd_1 = {"k_1": FrozenDict({"k_2": "v_2"})}
    fd_2 = pickle.loads(pickle.dumps(fd_1))
    assert set(fd_2.keys()) == {"k_1"}
    assert isinstance(fd_2["k_1"], FrozenDict)
    assert set(fd_2["k_1"].keys()) == {"k_2"}
    assert fd_2["k_1"]["k_2"] == "v_2"


def test_3():
    fd_1 = FrozenDict({"k_1": FrozenDict({"k_2": "v_2"})})
    fd_2 = pickle.loads(pickle.dumps(fd_1))
    assert set(fd_2.keys()) == {"k_1"}
    assert isinstance(fd_2["k_1"], FrozenDict)
    assert set(fd_2["k_1"].keys()) == {"k_2"}
    assert fd_2["k_1"]["k_2"] == "v_2"


def test_4():
    fd_1 = NoCopyFrozenDict({"k_1": NoCopyFrozenDict({"k_2": "v_2"})})
    fd_2 = pickle.loads(pickle.dumps(fd_1))
    assert set(fd_2.keys()) == {"k_1"}
    assert isinstance(fd_2["k_1"], FrozenDict)
    assert set(fd_2["k_1"].keys()) == {"k_2"}
    assert fd_2["k_1"]["k_2"] == "v_2"
