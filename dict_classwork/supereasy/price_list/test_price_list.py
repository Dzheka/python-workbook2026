import threading

import pytest

price_list = pytest.importorskip("price_list", reason="price_list.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(price_list, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")

    def limited(*args):
        result = {}

        def run():
            try:
                result["value"] = func(*args)
            except Exception as error:  # re-raised below, in the test itself
                result["error"] = error

        worker = threading.Thread(target=run, daemon=True)
        worker.start()
        worker.join(TIME_LIMIT)
        if worker.is_alive():
            pytest.fail(f"{name}{args} did not finish in {TIME_LIMIT}s: endless loop?")
        if "error" in result:
            raise result["error"]
        return result["value"]

    return limited


PRICES = {"bread": 4, "milk": 9, "tea": 15, "sugar": 12}


@pytest.mark.parametrize(
    "prices, basket, expected",
    [
        (PRICES, ["bread", "milk", "bread"], 17),
        (PRICES, ["bread", "cake"], 4),
        (PRICES, [], 0),
        (PRICES, ["tea", "sugar", "milk", "bread"], 40),
        ({}, ["bread"], 0),
    ],
)
def test_total(prices, basket, expected):
    assert function("total")(prices, basket) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        (PRICES, "bread"),
        ({"tea": 15, "milk": 9}, "milk"),
        ({"rice": 7, "beans": 7, "salt": 3, "oil": 3}, "oil"),
        ({"apple": 5}, "apple"),
        ({}, None),
    ],
)
def test_cheapest(prices, expected):
    assert function("cheapest")(prices) == expected
