import threading

import pytest

inventory = pytest.importorskip("inventory", reason="inventory.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(inventory, name, None)
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


STOCK = {"apples": 10, "pears": 4, "plums": 7}


@pytest.mark.parametrize(
    "stock, delivery, expected",
    [
        (
            STOCK,
            {"pears": 6, "kiwi": 3},
            {"apples": 10, "pears": 10, "plums": 7, "kiwi": 3},
        ),
        (STOCK, {}, STOCK),
        ({}, {"kiwi": 2}, {"kiwi": 2}),
        ({"a": 1}, {"a": 1}, {"a": 2}),
    ],
)
def test_restock(stock, delivery, expected):
    assert function("restock")(stock, delivery) == expected


@pytest.mark.parametrize(
    "stock, order, expected",
    [
        (STOCK, {"apples": 3, "pears": 4}, {"apples": 7, "plums": 7}),
        (STOCK, {"apples": 3, "pears": 5}, None),
        (STOCK, {"kiwi": 1}, None),
        (STOCK, {}, STOCK),
        (STOCK, {"apples": 10, "pears": 4, "plums": 7}, {}),
    ],
)
def test_sell(stock, order, expected):
    assert function("sell")(stock, order) == expected


def test_inputs_are_not_changed():
    stock = {"apples": 10, "pears": 4}
    delivery = {"pears": 1}
    order = {"apples": 2, "pears": 9}
    function("restock")(stock, delivery)
    function("sell")(stock, {"apples": 10})
    function("sell")(stock, order)
    assert stock == {"apples": 10, "pears": 4}
    assert delivery == {"pears": 1}
    assert order == {"apples": 2, "pears": 9}
