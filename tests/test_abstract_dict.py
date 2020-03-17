from typing import Mapping

from frozendict import frozendict, FrozenDict, AbstractDict


def test_isinstance():
    fd = frozendict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, Mapping)
    assert isinstance(fd, AbstractDict)

    d = {'test': 0}
    assert isinstance(d, Mapping)
    assert isinstance(d, AbstractDict)
