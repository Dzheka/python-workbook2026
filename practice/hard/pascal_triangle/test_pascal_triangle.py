import threading

import pytest

pascal_triangle = pytest.importorskip(
    "pascal_triangle", reason="pascal_triangle.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(pascal_triangle, name, None)
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
    "n, k, expected",
    [
        (0, 0, 1),
        (4, 2, 6),
        (5, 0, 1),
        (5, 5, 1),
        (10, 3, 120),
        (20, 10, 184756),
        (5, 6, 0),
        (5, -1, 0),
    ],
)
def test_binomial(n, k, expected):
    assert function("binomial")(n, k) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "1"),
        (1, "1 1"),
        (4, "1 4 6 4 1"),
        (5, "1 5 10 10 5 1"),
        (10, "1 10 45 120 210 252 210 120 45 10 1"),
    ],
)
def test_pascal_row(n, expected):
    assert function("pascal_row")(n) == expected


@pytest.mark.parametrize(
    "rows, expected",
    [
        (1, "1"),
        (3, "  1\n 1 1\n1 2 1"),
        (5, "    1\n   1 1\n  1 2 1\n 1 3 3 1\n1 4 6 4 1"),
        (6, "      1\n     1 1\n    1 2 1\n   1 3 3 1\n  1 4 6 4 1\n1 5 10 10 5 1"),
        (
            7,
            "       1\n      1 1\n     1 2 1\n    1 3 3 1\n   1 4 6 4 1\n 1 5 10 10 5 1\n1 6 15 20 15 6 1",
        ),
        (
            8,
            "         1\n        1 1\n       1 2 1\n      1 3 3 1\n     1 4 6 4 1\n   1 5 10 10 5 1\n 1 6 15 20 15 6 1\n1 7 21 35 35 21 7 1",
        ),
    ],
)
def test_pascal_triangle(rows, expected):
    assert function("pascal_triangle")(rows) == expected
