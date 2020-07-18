# test_performance_a

from datetime import datetime
from pytest import mark

from frozendict import FrozenDict


@mark.skip
def test_performance_a_1():
    repeat = 100000
    updates = 3
    frozendict_updates(repeat, updates)
    dict_updates(repeat, updates)


def frozendict_updates(repeat, updates):
    start_time = datetime.now()
    for i in range(repeat):
        dct = FrozenDict()
        for j in range(updates):
            dct = FrozenDict({
                **dct,
                f"k_{j}": j,
            })
    lapsed = (datetime.now() - start_time).seconds
    print(f"* frozendict with {updates} updates: {lapsed}s")


def dict_updates(repeat, updates):
    start_time = datetime.now()
    for i in range(repeat):
        dct = dict()
        for j in range(updates):
            dct[f"k_{j}"] = j
        fd = FrozenDict(dct)  # noqa: F841
    lapsed = (datetime.now() - start_time).seconds
    print(f"* dict with {updates} updates: {lapsed}s")
