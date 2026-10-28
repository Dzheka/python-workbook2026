import threading

import pytest

stock_prices = pytest.importorskip(
    "stock_prices", reason="stock_prices.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(stock_prices, name, None)
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
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3], 0),
        ([], 0),
        ([5], 0),
        ([2, 4, 1, 7], 6),
        ([3, 3, 3], 0),
        ([1, 2, 3, 4, 5], 4),
    ],
)
def test_max_profit(prices, expected):
    assert function("max_profit")(prices) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], [1, 4]),
        ([7, 6, 4, 3], []),
        ([], []),
        ([2, 4, 1, 7], [2, 3]),
        ([1, 5, 1, 5], [0, 1]),
        ([3, 3, 3], []),
    ],
)
def test_best_days(prices, expected):
    assert function("best_days")(prices) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([3, 5, 5, 2], "+=-"),
        ([10], ""),
        ([], ""),
        ([1, 2, 3], "++"),
        ([9, 1, 1, 4], "-=+"),
    ],
)
def test_trend(prices, expected):
    assert function("trend")(prices) == expected
