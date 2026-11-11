import threading


import pytest

sudoku_check = pytest.importorskip(
    "sudoku_check", reason="sudoku_check.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(sudoku_check, name, None)
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
    "row, expected",
    [
        ([5, 3, 0, 0, 7, 0, 0, 0, 0], [1, 2, 4, 6, 8, 9]),
        ([5, 3, 4, 6, 7, 8, 9, 1, 2], []),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([9, 9, 9, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8]),
    ],
)
def test_missing(row, expected):
    assert function("missing")(row) == expected


@pytest.mark.parametrize(
    "row, expected",
    [
        ([5, 3, 4, 6, 7, 8, 9, 1, 2], True),
        ([5, 3, 4, 6, 7, 8, 9, 1, 1], False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 0], False),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], True),
    ],
)
def test_valid_group(row, expected):
    assert function("valid_group")(row) is expected


@pytest.mark.parametrize(
    "row, expected",
    [
        ([5, 3, 0, 0, 7, 0, 0, 0, 5], True),
        ([5, 3, 0, 0, 7, 0, 0, 0, 0], False),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], False),
        ([1, 2, 3, 4, 5, 6, 7, 9, 9], True),
    ],
)
def test_has_conflict(row, expected):
    assert function("has_conflict")(row) is expected
