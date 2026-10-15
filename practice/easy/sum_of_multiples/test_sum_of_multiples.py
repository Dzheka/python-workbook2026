import threading

import pytest

sum_of_multiples = pytest.importorskip(
    "sum_of_multiples", reason="sum_of_multiples.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(sum_of_multiples, name, None)
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
    "limit, a, b, expected",
    [
        (10, 3, 5, 4),
        (16, 3, 5, 7),
        (1, 3, 5, 0),
        (20, 2, 4, 9),
        (100, 7, 11, 22),
    ],
)
def test_count_multiples(limit, a, b, expected):
    assert function("count_multiples")(limit, a, b) == expected


@pytest.mark.parametrize(
    "limit, a, b, expected",
    [
        (10, 3, 5, 23),
        (16, 3, 5, 60),
        (1, 3, 5, 0),
        (20, 2, 4, 90),
        (1000, 3, 5, 233168),
        (100, 7, 11, 1153),
    ],
)
def test_sum_multiples(limit, a, b, expected):
    assert function("sum_multiples")(limit, a, b) == expected
