import threading

import pytest

max_digit = pytest.importorskip("max_digit", reason="max_digit.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(max_digit, name, None)
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
    "n, expected",
    [
        (5, 5),
        (0, 0),
        (1234, 4),
        (90817, 9),
        (-472, 7),
        (111, 1),
    ],
)
def test_max_digit(n, expected):
    assert function("max_digit")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 5),
        (0, 0),
        (1234, 1),
        (90817, 0),
        (-472, 2),
        (111, 1),
        (987, 7),
    ],
)
def test_min_digit(n, expected):
    assert function("min_digit")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 0),
        (90817, 9),
        (-472, 5),
        (111, 0),
        (19, 8),
    ],
)
def test_digit_range(n, expected):
    assert function("digit_range")(n) == expected
