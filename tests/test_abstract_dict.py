from typing import Mapping

from frozendict import AbstractDict, FrozenDict, frozendict


def test_isinstance():
    fd = frozendict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, frozendict)
    assert isinstance(fd, Mapping)
    assert isinstance(fd, AbstractDict)

    d = {'test': 0}
    assert isinstance(d, Mapping)
    assert isinstance(d, AbstractDict)


def test_abstract_dict_typing_1():
    dict()
    dct: AbstractDict[str, str] = {'k_1': 'v_1'}
    assert dct['k_1'] == 'v_1'


def test_abstract_dict_typing_2():
    def foo(dct: AbstractDict[str, str]):
        assert dct['k_1'] == 'v_1'

    foo({'k_1': 'v_1'})
