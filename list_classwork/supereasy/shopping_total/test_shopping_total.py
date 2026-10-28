import threading

import pytest

shopping_total = pytest.importorskip(
    "shopping_total", reason="shopping_total.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(shopping_total, name, None)
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


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([10, 20, 5], 35),
        ([], 0),
        ([99], 99),
    ],
)
def test_total(prices, expected):
    assert function("total")(prices) == expected


@pytest.mark.parametrize(
    "prices, money, expected",
    [
        ([10, 20, 5], 50, "yes"),
        ([10, 20, 5], 35, "yes"),
        ([10, 20, 5], 30, "no"),
        ([], 0, "yes"),
    ],
)
def test_can_afford(prices, money, expected):
    assert function("can_afford")(prices, money) == expected
