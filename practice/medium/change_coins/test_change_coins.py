import threading

import pytest

change_coins = pytest.importorskip(
    "change_coins", reason="change_coins.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(change_coins, name, None)
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
    "amount, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (88, 6),
        (125, 4),
        (99, 6),
        (100, 2),
    ],
)
def test_count_coins(amount, expected):
    assert function("count_coins")(amount) == expected


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, ""),
        (1, "1x1"),
        (4, "2x2"),
        (88, "1x50 1x20 1x10 1x5 1x2 1x1"),
        (125, "2x50 1x20 1x5"),
        (99, "1x50 2x20 1x5 2x2"),
        (100, "2x50"),
    ],
)
def test_coin_breakdown(amount, expected):
    assert function("coin_breakdown")(amount) == expected


@pytest.mark.parametrize(
    "amount, max_coins, expected",
    [
        (88, 4, False),
        (88, 3, False),
        (0, 0, True),
        (125, 4, True),
        (99, 6, True),
        (99, 5, False),
    ],
)
def test_can_pay(amount, max_coins, expected):
    assert function("can_pay")(amount, max_coins) is expected
