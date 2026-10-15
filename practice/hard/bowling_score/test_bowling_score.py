import threading

import pytest

bowling_score = pytest.importorskip(
    "bowling_score", reason="bowling_score.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(bowling_score, name, None)
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
    "rolls, i, expected",
    [
        ("X", 0, 10),
        ("9-", 0, 9),
        ("9-", 1, 0),
        ("7/", 1, 3),
        ("3/", 1, 7),
        ("X7/", 2, 3),
    ],
)
def test_roll_value(rolls, i, expected):
    assert function("roll_value")(rolls, i) == expected


@pytest.mark.parametrize(
    "rolls, expected",
    [
        ("--------------------", 0),
        ("9-9-9-9-9-9-9-9-9-9-", 90),
        ("XXXXXXXXXXXX", 300),
        ("5/5/5/5/5/5/5/5/5/5/5", 150),
        ("X7/9-X-88/-6XXX81", 167),
        ("11111111111111111111", 20),
        ("X--------------------", 10),
        ("------------------X12", 13),
    ],
)
def test_score(rolls, expected):
    assert function("score")(rolls) == expected


@pytest.mark.parametrize(
    "rolls, expected",
    [
        ("XXXXXXXXXXXX", True),
        ("XXXXXXXXXXX9", False),
        ("9-9-9-9-9-9-9-9-9-9-", False),
    ],
)
def test_is_perfect_game(rolls, expected):
    assert function("is_perfect_game")(rolls) is expected
