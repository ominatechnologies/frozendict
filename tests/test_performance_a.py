# test_performance_a

from datetime import datetime

from pytest import mark

from frozendict import FrozenDict


@mark.skip("Performance test.")
def test_performance_a_1():
    repeat = 100000
    updates = 3
    frozendict_updates(repeat, updates)
    dict_updates(repeat, updates)


def frozendict_updates(repeat, updates):
    start_time = datetime.now()
    for _ in range(repeat):
        FrozenDict({f"k_{j}": j for j in range(updates)})
    lapsed = (datetime.now() - start_time).seconds
    print(f"* frozendict with {updates} updates: {lapsed}s")  # noqa: T001


def dict_updates(repeat, updates):
    start_time = datetime.now()
    for _ in range(repeat):
        FrozenDict({f"k_{j}": j for j in range(updates)})
    lapsed = (datetime.now() - start_time).seconds
    print(f"* dict with {updates} updates: {lapsed}s")  # noqa: T001
