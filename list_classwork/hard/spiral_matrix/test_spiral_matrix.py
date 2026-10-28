import threading

import pytest

spiral_matrix = pytest.importorskip(
    "spiral_matrix", reason="spiral_matrix.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(spiral_matrix, name, None)
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
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[7]], [7]),
        ([], []),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8],
        ),
    ],
)
def test_spiral_order(matrix, expected):
    assert function("spiral_order")(matrix) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [[1]]),
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
    ],
)
def test_spiral_matrix(n, expected):
    assert function("spiral_matrix")(n) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2], [4, 3]], "1 2\n4 3"),
        ([[7]], "7"),
        ([[1, 2, 3]], "1 2 3"),
        ([[10, 2], [3, 40]], "10 2\n3 40"),
    ],
)
def test_format_matrix(matrix, expected):
    assert function("format_matrix")(matrix) == expected


def test_spiral_order_reads_back_spiral_matrix():
    assert function("spiral_order")(function("spiral_matrix")(5)) == list(range(1, 26))
