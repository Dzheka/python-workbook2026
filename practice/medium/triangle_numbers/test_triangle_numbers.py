import threading

import pytest

triangle_numbers = pytest.importorskip(
    "triangle_numbers", reason="triangle_numbers.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(triangle_numbers, name, None)
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
        (1, 1),
        (4, 10),
        (10, 55),
        (100, 5050),
        (0, 0),
    ],
)
def test_nth_triangle(n, expected):
    assert function("nth_triangle")(n) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (1, 1),
        (10, 4),
        (55, 10),
        (5050, 100),
        (11, -1),
        (54, -1),
        (2, -1),
    ],
)
def test_triangle_index(x, expected):
    assert function("triangle_index")(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (1, True),
        (3, True),
        (6, True),
        (28, True),
        (2, False),
        (27, False),
        (5050, True),
    ],
)
def test_is_triangular(x, expected):
    assert function("is_triangular")(x) is expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 10, 4),
        (1, 100, 13),
        (11, 14, 0),
        (1, 1000, 44),
    ],
)
def test_count_triangular(start, end, expected):
    assert function("count_triangular")(start, end) == expected
