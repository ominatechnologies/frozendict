from frozendict import AbstractDict, FrozenDict


def test_abstract_dict_typing_1():
    dct: AbstractDict[str, str] = {'k_1': 'v_1'}
    assert dct['k_1'] == 'v_1'

    dct: AbstractDict[str, str] = FrozenDict({'k_1': 'v_1'})
    assert dct['k_1'] == 'v_1'


def test_abstract_dict_typing_2():
    def f_1(dct: AbstractDict[str, str]):
        assert dct['k_1'] == 'v_1'
        f_2(dct['k_1'])

        # Mypy should not accept the following, but there is no equivalent to
        # "pytest.raises" for asserting such failures, which is why the
        # following is commented out.
        #
        # f_3(dct['k_1'])

    def f_2(val: str):
        # print(f"f_2 {val=}")
        return val

    # noinspection PyUnusedLocal
    def f_3(val: int):
        # print(f"f_3 {val=}")
        return val

    f_1({'k_1': 'v_1'})
    f_1(FrozenDict({'k_1': 'v_1'}))


def test_abstract_dict_typing_3():
    class ClassA:
        pass

    class ClassB(ClassA):
        pass

    def f_1(dct: AbstractDict[str, ClassA]):
        f_2(dct['k_1'])

        # Mypy should not accept the following, but there is no equivalent to
        # "pytest.raises" for asserting such failures, which is why the
        # following is commented out.
        #
        # f_3(dct['k_1'])

    def f_2(val: ClassA):
        # print(f"f_2 {val=}")
        return val

    # noinspection PyUnusedLocal
    def f_3(val: int):
        # print(f"f_3 {val=}")
        return val

    f_1({'k_1': ClassA()})
    f_1(FrozenDict({'k_1': ClassA()}))

    f_1({'k_1': ClassB()})
    f_1(FrozenDict({'k_1': ClassB()}))


def test_abstract_dict_typing_4():
    class ClassA:
        pass

    class ClassB(ClassA):
        pass

    def f_1(dct: AbstractDict[str, ClassB]):
        f_2(dct)

    def f_2(dct: AbstractDict[str, ClassA]):
        return dct

    f_1({'k_1': ClassB()})
    f_1(FrozenDict({'k_1': ClassB()}))
