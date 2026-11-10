import threading

import pytest

bingo = pytest.importorskip("bingo", reason="bingo.py not implemented")

TIME_LIMIT = 5

CARD = [
    [5, 18, 33, 48, 64],
    [12, 21, 31, 52, 70],
    [3, 26, 0, 47, 61],
    [9, 17, 38, 55, 68],
    [14, 29, 41, 50, 75],
]


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(bingo, name, None)
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
    "card, called, expected",
    [
        (CARD, [5, 99, 21], 3),
        (CARD, [], 1),
        (CARD, [5, 5, 5], 2),
        ([[1, 2], [3, 4]], [4, 3, 2, 1], 4),
        ([[1, 2], [3, 4]], [7, 8], 0),
    ],
)
def test_marked(card, called, expected):
    assert function("marked")(card, called) == expected


@pytest.mark.parametrize(
    "card, called, expected",
    [
        (CARD, [3, 26, 47, 61], True),
        (CARD, [5, 21, 55, 75], True),
        (CARD, [5, 12, 3, 9], False),
        (CARD, [5, 12, 3, 9, 14], True),
        (CARD, [64, 52, 17, 14], True),
        (CARD, [33, 31, 38, 41], True),
        (CARD, [], False),
        (CARD, [5, 18, 33, 48, 70], False),
        ([[1, 2], [3, 4]], [1, 2], True),
        ([[1, 2], [3, 4]], [1, 3], True),
        ([[1, 2], [3, 4]], [2, 3], True),
        ([[1, 2], [3, 4]], [1, 99], False),
    ],
)
def test_has_bingo(card, called, expected):
    assert function("has_bingo")(card, called) is expected
