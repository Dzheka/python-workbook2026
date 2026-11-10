import threading

import pytest

matrix_ops = pytest.importorskip("matrix_ops", reason="matrix_ops.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(matrix_ops, name, None)
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
        ([[1, 2, 3], [4, 5, 6]], [6, 15]),
        ([[7]], [7]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[-1, 1], [0, 0]], [0, 0]),
    ],
)
def test_row_sums(matrix, expected):
    assert function("row_sums")(matrix) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [5, 7, 9]),
        ([[7]], [7]),
        ([[1], [2], [3]], [6]),
        ([[1, 2, 3]], [1, 2, 3]),
    ],
)
def test_col_sums(matrix, expected):
    assert function("col_sums")(matrix) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([[7]], [[7]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
    ],
)
def test_transpose(matrix, expected):
    assert function("transpose")(matrix) == expected


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2], [3, 4]], 5),
        ([[7]], 7),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
        ([[0, 9], [9, 0]], 0),
    ],
)
def test_diagonal_sum(matrix, expected):
    assert function("diagonal_sum")(matrix) == expected


def test_input_is_not_changed():
    matrix = [[1, 2], [3, 4]]
    function("transpose")(matrix)
    assert matrix == [[1, 2], [3, 4]]
