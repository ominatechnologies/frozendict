from typing import Mapping, Optional, Union

from pytest import raises

from frozendict import AbstractDict, FrozenDict, frozendict


def test_init_1():
    assert frozendict is FrozenDict

    fd: AbstractDict = FrozenDict()
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, AbstractDict)
    assert isinstance(fd, Mapping)


def test_init_3():
    fd = FrozenDict({})
    assert isinstance(fd, FrozenDict)
    assert isinstance(fd, AbstractDict)
    assert isinstance(fd, Mapping)


def test_init_4():
    fd: FrozenDict[str, int] = FrozenDict({'k_1': 123})
    assert fd.get('k_1') == 123


def test_init_5():
    fd: FrozenDict[str, str] = FrozenDict({'k_1': '0'})
    assert fd.get('k_1') == '0'


def test_init_6():
    fd: FrozenDict[int, int] = FrozenDict({1: 0})
    assert fd.get(1) == 0


def test_init_7():
    fd: FrozenDict[str, Union[int, str]] = FrozenDict({
        'k_1': 0,
        'k_2': 'v_2'
    })
    assert fd.get('k_1') == 0
    assert fd.get('k_2') == 'v_2'


def test_init_non_dict():
    with raises(TypeError):
        # noinspection PyTypeChecker
        FrozenDict({'1', '0'})

    with raises(TypeError):
        # noinspection PyTypeChecker
        FrozenDict({1, 0})


def test_init_homogeneous():
    with raises(TypeError):
        FrozenDict({'k_1': 0, 'k_2': '1'}, homogeneous_type=True)
    with raises(TypeError):
        FrozenDict(k_1=0, k_2='1', homogeneous_type=True)
    with raises(TypeError):
        FrozenDict({'k_1': 0, 1: 1}, homogeneous_type=True)
    with raises(TypeError):
        FrozenDict({'k_1': 0, 1: '1'}, homogeneous_type=True)


def test_init_kwargs():
    fd: FrozenDict[str, int] = FrozenDict(k_1=0)
    assert fd.keys() == {'k_1'}
    assert fd.get('k_1') == 0

    fd: FrozenDict[str, int] = FrozenDict(k_1=0, k_2=1)
    assert fd.keys() == {'k_1', 'k_2'}
    assert fd.get('k_1') == 0
    assert fd.get('k_2') == 1

    fd: FrozenDict[str, int] = FrozenDict(k_1=0, k_2=1)
    assert fd.keys() == {'k_1', 'k_2'}
    assert fd.get('k_1') == 0
    assert fd.get('k_2') == 1

    fd: FrozenDict[str, Union[int, str]] = FrozenDict(k_1=0, k_2='1')
    assert fd.keys() == {'k_1', 'k_2'}
    assert fd.get('k_1') == 0
    assert fd.get('k_2') == '1'


def test_init_no_none_value():
    fd: FrozenDict[str, int] = FrozenDict({'k_1': 0}, remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('k_1') == 0

    fd: FrozenDict[str, int] = FrozenDict({'k_1': 0, 'k_2': None},
                                          remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('k_1') == 0

    fd: FrozenDict[str, int] = FrozenDict({'k_1': 0, 'k_2': None},
                                          remove_none_value=True,
                                          homogeneous_type=True)
    assert len(fd) == 1
    assert fd.get('k_1') == 0

    fd: FrozenDict[str, int] = FrozenDict(k_1=0, k_2=None,
                                          remove_none_value=True)
    assert len(fd) == 1
    assert fd.get('k_1') == 0

    fd: FrozenDict[str, int] = FrozenDict(k_1=0, k_2=None,
                                          remove_none_value=True,
                                          homogeneous_type=True)
    assert len(fd) == 1
    assert fd.get('k_1') == 0


def test_get():
    fd: FrozenDict[str, int] = FrozenDict({'k_1': 0})
    assert fd.get('k_1') == 0
    assert not fd.get('k_2')


def test_len():
    fd1: FrozenDict = FrozenDict()
    assert len(fd1) == 0

    fd2: FrozenDict[str, int] = FrozenDict({'k_1': 0})
    assert len(fd2) == 1

    fd3: FrozenDict[str, int] = FrozenDict({'k_1': 0, 'k_2': 1})
    assert len(fd3) == 2


def test_singleton():
    assert FrozenDict() is FrozenDict()
    assert FrozenDict() is FrozenDict({})
    assert FrozenDict({}) is FrozenDict()
    assert FrozenDict({}) is FrozenDict({})

    assert FrozenDict({'k_1': 'test'}) is not FrozenDict()
    assert FrozenDict() is not FrozenDict({'k_1': 'test'})
    assert FrozenDict() is not FrozenDict(k_1=0)
    assert FrozenDict({'k_1': 'test'}) is not FrozenDict({'k_1': 'test'})
    assert FrozenDict(k_1=0) is not FrozenDict({'k_1': 'test'})
    assert FrozenDict(k_1=0) is not FrozenDict(k_1=0)


def test_equality():
    assert FrozenDict() == FrozenDict()
    assert FrozenDict({'k_1': 0}) == FrozenDict({'k_1': 0})
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd == FrozenDict(d)
    assert FrozenDict() != FrozenDict({'k_1': 0})
    assert FrozenDict({'k_1': 1}) != FrozenDict({'k_1': 0})
    assert FrozenDict({'k_2': 0}) != FrozenDict({'k_1': 0})


def test_hash():
    assert hash(FrozenDict()) == hash(FrozenDict())
    assert hash(FrozenDict({'k_1': 0})) == hash(FrozenDict({'k_1': 0}))
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert hash(fd) == hash(FrozenDict(d))
    assert hash(fd) == hash(fd)
    assert hash(FrozenDict()) != hash(FrozenDict({'k_1': 0}))
    assert hash(FrozenDict({'k_1': 1})) != hash(FrozenDict({'k_1': 0}))
    assert hash(FrozenDict({'k_2': 0})) != hash(FrozenDict({'k_1': 0}))


def test_keys():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd.keys() == d.keys()


def test_items():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd.items() == d.items()


def test_values():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert list(fd.values()) == list(d.values())


def test_union():
    d = {'k_1': 0, 'k_2': 1}
    assert FrozenDict({'k_1': 0}) | FrozenDict({'k_2': 1}) == d
    assert FrozenDict({'k_1': 0}) | {'k_2': 1} == d
    assert FrozenDict({'k_1': 0}).union(FrozenDict({'k_2': 1})) == d
    assert FrozenDict({'k_1': 0}).union({'k_2': 1}) == d

    with raises(NotImplementedError):
        FrozenDict() | ('k_1', 0)
    with raises(NotImplementedError):
        FrozenDict().union(('k_1', 0))


def test_intersection():
    d1 = {'k_1': 0, 'k_2': 1}
    d2 = {'k_1': 0, 'k_3': 2}
    assert FrozenDict(d1) & FrozenDict(d2) == {'k_1': 0}
    assert FrozenDict(d1) & d2 == {'k_1': 0}
    assert FrozenDict(d1).intersection(FrozenDict(d2)) == {'k_1': 0}
    assert FrozenDict(d1).intersection(d2) == {'k_1': 0}

    with raises(NotImplementedError):
        FrozenDict() & ('k_1', 0)
    with raises(NotImplementedError):
        FrozenDict().intersection(('k_1', 0))


def test_imutable():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    assert fd.items() == d.items()
    d['test3'] = 3
    assert d.get('test3') == 3
    assert not fd.get('test3')

    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({'k_1': fd})
    assert ffd.get('k_1') == fd

    assert len({fd, fd, fd, fd, fd, fd}) == 1


def test_imutable_no_copy():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = frozendict(d, no_copy=True)
    assert fd.items() == d.items()
    d['k_3'] = 3
    assert d.get('k_3') == 3
    assert fd.get('k_3') == 3


def test_repr():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({'k_1': fd})
    pfd = "<FrozenDict {'k_1': 0, 'k_2': 1}>"
    pffd = "<FrozenDict {'k_1': <FrozenDict {'k_1': 0, 'k_2': 1}>}>"
    assert fd.__repr__() == pfd
    assert ffd.__repr__() == pffd


def test_serialize():
    d = {'k_1': 0, 'k_2': 1}
    fd: FrozenDict[str, int] = FrozenDict(d)
    ffd: FrozenDict[str, FrozenDict[str, int]] = FrozenDict({'k_1': fd})
    s_fd: Mapping[str, int] = fd.serialize()
    s_ffd: Mapping[str, Mapping[str, int]] = ffd.serialize()
    assert s_fd == d
    assert s_ffd == {'k_1': d}


def test_typing_1():
    class ClassA:
        pass

    def f_1(dct: FrozenDict[str, Optional[ClassA]]):
        # f_2(dct['k_1'])
        return dct

    dct_1: FrozenDict[str, ClassA] = FrozenDict({'k_1': ClassA()})
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

    f_1(FrozenDict({'k_1': ClassB()}))


def test_typing_3():
    class ClassA:
        pass

    def f_1(dct: FrozenDict[str, ClassA]):
        f_2(dct)

    def f_2(dct: FrozenDict[str, Optional[ClassA]]):
        return dct

    f_1(FrozenDict({'k_1': ClassA()}))
