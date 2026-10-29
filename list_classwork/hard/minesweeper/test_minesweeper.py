import threading

import pytest

minesweeper = pytest.importorskip(
    "minesweeper", reason="minesweeper.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(minesweeper, name, None)
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


FIELD = ["*..", "...", ".*."]


@pytest.mark.parametrize(
    "field, r, c, expected",
    [
        (FIELD, 1, 1, 2),
        (FIELD, 0, 2, 0),
        (FIELD, 0, 1, 1),
        (FIELD, 2, 0, 1),
        (["***", "*.*", "***"], 1, 1, 8),
        (["*"], 0, 0, 0),
    ],
)
def test_count_mines(field, r, c, expected):
    assert function("count_mines")(field, r, c) == expected


@pytest.mark.parametrize(
    "field, expected",
    [
        (FIELD, ["*1.", "221", "1*1"]),
        (["..."], ["..."]),
        (["***", "*.*", "***"], ["***", "*8*", "***"]),
        ([".*.*."], ["1*2*1"]),
        (["*...", "..*.", "...."], ["*211", "12*1", ".111"]),
    ],
)
def test_annotate(field, expected):
    assert function("annotate")(field) == expected


@pytest.mark.parametrize(
    "field, expected",
    [
        (FIELD, 1),
        (["..."], 3),
        (["***", "*.*", "***"], 0),
        (["*...", "..*.", "...."], 1),
    ],
)
def test_safe_squares(field, expected):
    assert function("safe_squares")(field) == expected


def test_annotate_does_not_change_input():
    field = list(FIELD)
    function("annotate")(field)
    assert field == FIELD
