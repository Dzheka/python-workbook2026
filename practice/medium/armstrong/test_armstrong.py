import threading

import pytest

armstrong = pytest.importorskip("armstrong", reason="armstrong.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(armstrong, name, None)
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
        (0, 1),
        (7, 1),
        (10, 2),
        (153, 3),
        (99999, 5),
    ],
)
def test_count_digits(n, expected):
    assert function("count_digits")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (9, True),
        (10, False),
        (153, True),
        (154, False),
        (370, True),
        (9474, True),
        (9475, False),
    ],
)
def test_is_armstrong(n, expected):
    assert function("is_armstrong")(n) is expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 9, 9),
        (1, 1000, 13),
        (100, 999, 4),
        (10, 99, 0),
        (1000, 10000, 3),
    ],
)
def test_count_armstrong(start, end, expected):
    assert function("count_armstrong")(start, end) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (9, 153),
        (153, 370),
        (407, 1634),
        (1634, 8208),
        (9474, 54748),
    ],
)
def test_next_armstrong(n, expected):
    assert function("next_armstrong")(n) == expected
