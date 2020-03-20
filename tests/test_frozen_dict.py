from typing import Mapping, Union

from pytest import raises

from frozendict import FrozenDict, frozendict, AbstractDict


def test_init():
    fd = frozendict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, Mapping)
    assert isinstance(fd, AbstractDict)

    fd = FrozenDict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, Mapping)
    assert isinstance(fd, AbstractDict)

    fd = frozendict({})
    assert isinstance(fd, FrozenDict)

    fd: FrozenDict[str, int] = frozendict({'test': 0})
    assert fd.get('test') == 0

    fd: FrozenDict[str, str] = frozendict({'test': '0'})
    assert fd.get('test') == '0'

    fd: FrozenDict[int, int] = frozendict({1: 0})
    assert fd.get(1) == 0

    fd: FrozenDict[str, Union[int, str]] = frozendict({
        'test': 0,
        'test1': '1'
    })
    assert fd.get('test') == 0
    assert fd.get('test1') == '1'


def test_init_non_dict():
    with raises(TypeError):
        frozendict({'1', '0'})

    with raises(TypeError):
        frozendict({1, 0})


def test_init_homogeneous():
    with raises(TypeError):
        frozendict({'test': 0, 'test1': '1'}, homogeneous_type=True)
    with raises(TypeError):
        frozendict(test=0, test1='1', homogeneous_type=True)


def test_init_kwargs():
    fd: FrozenDict[str, int] = FrozenDict(test=0)
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = frozendict(test=0)
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = FrozenDict(test=0, test1=1)
    assert fd.get('test') == 0
    assert fd.get('test1') == 1

    fd: FrozenDict[str, int] = frozendict(test=0, test1=1)
    assert fd.get('test') == 0
    assert fd.get('test1') == 1

    fd: FrozenDict[str, Union[int, str]] = frozendict(test=0, test1='1')
    assert fd.get('test') == 0
    assert fd.get('test1') == '1'


def test_init_no_none_value():
    fd: FrozenDict[str, int] = frozendict({'test': 0}, remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = frozendict({'test': 0, 'test1': None},
                                          remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = frozendict({'test': 0, 'test1': None},
                                          remove_none_value=True,
                                          homogeneous_type=True)
    assert len(fd) == 1
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = frozendict(test=0, test1=None,
                                          remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('test') == 0

    fd: FrozenDict[str, int] = frozendict(test=0, test1=None,
                                          remove_none_value=True,
                                          homogeneous_type=True)
    assert len(fd) == 1
    assert fd.get('test') == 0


def test_get():
    fd: FrozenDict[str, int] = frozendict({'test': 0})
    assert fd.get('test') == 0
    assert not fd.get('test1')


def test_len():
    fd1: FrozenDict = frozendict()
    assert len(fd1) == 0

    fd2: FrozenDict[str, int] = frozendict({'test': 0})
    assert len(fd2) == 1

    fd3: FrozenDict[str, int] = frozendict({'test': 0, 'test1': 1})
    assert len(fd3) == 2


def test_singleton():
    assert frozendict() is frozendict()
    assert frozendict({}) is not frozendict()
    assert frozendict({}) is not frozendict({})


def test_equality():
    assert frozendict() == frozendict()
    assert frozendict({'test': 0}) == frozendict({'test': 0})
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert fd == frozendict(d)
    assert frozendict() != frozendict({'test': 0})
    assert frozendict({'test': 1}) != frozendict({'test': 0})
    assert frozendict({'test1': 0}) != frozendict({'test': 0})


def test_hash():
    assert hash(frozendict()) == hash(frozendict())
    assert hash(frozendict({'test': 0})) == hash(frozendict({'test': 0}))
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert hash(fd) == hash(frozendict(d))
    assert hash(fd) == hash(fd)
    assert hash(frozendict()) != hash(frozendict({'test': 0}))
    assert hash(frozendict({'test': 1})) != hash(frozendict({'test': 0}))
    assert hash(frozendict({'test1': 0})) != hash(frozendict({'test': 0}))


def test_keys():
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert fd.keys() == d.keys()


def test_items():
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert fd.items() == d.items()


def test_values():
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert list(fd.values()) == list(d.values())


def test_union():
    d = {'test': 0, 'test1': 1}
    assert frozendict({'test': 0}) | frozendict({'test1': 1}) == d
    assert frozendict({'test': 0}) | {'test1': 1} == d
    assert frozendict({'test': 0}).union(frozendict({'test1': 1})) == d
    assert frozendict({'test': 0}).union({'test1': 1}) == d

    with raises(NotImplementedError):
        frozendict() | ('test', 0)
    with raises(NotImplementedError):
        frozendict().union(('test', 0))


def test_intersection():
    d1 = {'test': 0, 'test1': 1}
    d2 = {'test': 0, 'test2': 2}
    assert frozendict(d1) & frozendict(d2) == {'test': 0}
    assert frozendict(d1) & d2 == {'test': 0}
    assert frozendict(d1).intersection(frozendict(d2)) == {'test': 0}
    assert frozendict(d1).intersection(d2) == {'test': 0}

    with raises(NotImplementedError):
        frozendict() & ('test', 0)
    with raises(NotImplementedError):
        frozendict().intersection(('test', 0))


def test_imutable():
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    assert fd.items() == d.items()
    d['test3'] = 3
    assert d.get('test3') == 3
    assert not fd.get('test3')

    ffd: FrozenDict[str, FrozenDict[str, int]] = frozendict({'test': fd})
    assert ffd.get('test') == fd

    assert len({fd, fd, fd, fd, fd, fd}) == 1


def test_repr():
    d = {'test': 0, 'test1': 1}
    fd: FrozenDict[str, int] = frozendict(d)
    ffd: FrozenDict[str, FrozenDict[str, int]] = frozendict({'test': fd})
    pfd = "<FrozenDict {'test': 0, 'test1': 1}>"
    pffd = "<FrozenDict {'test': <FrozenDict {'test': 0, 'test1': 1}>}>"
    assert fd.__repr__() == pfd
    assert ffd.__repr__() == pffd
