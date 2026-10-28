import threading

import pytest

rock_paper_scissors = pytest.importorskip(
    "rock_paper_scissors", reason="rock_paper_scissors.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(rock_paper_scissors, name, None)
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
    "a, b, expected",
    [
        ("R", "S", True),
        ("S", "P", True),
        ("P", "R", True),
        ("S", "R", False),
        ("R", "R", False),
        ("P", "S", False),
    ],
)
def test_beats(a, b, expected):
    assert function("beats")(a, b) is expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("R", "S", 1),
        ("S", "R", 2),
        ("P", "P", 0),
        ("P", "R", 1),
        ("R", "P", 2),
    ],
)
def test_round_result(a, b, expected):
    assert function("round_result")(a, b) == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        ("RPS", "SPR", "1:1"),
        ("RRR", "PPP", "0:3"),
        ("", "", "0:0"),
        ("RSPRSP", "SPRSPR", "6:0"),
        ("RPSRPS", "RPSRPS", "0:0"),
        ("RRSSPP", "SPRPSR", "3:3"),
    ],
)
def test_match_score(first, second, expected):
    assert function("match_score")(first, second) == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        ("RPS", "SPR", "draw"),
        ("RRR", "PPP", "second"),
        ("RSP", "SPR", "first"),
        ("PPPP", "RRRR", "first"),
        ("", "", "draw"),
    ],
)
def test_match_winner(first, second, expected):
    assert function("match_winner")(first, second) == expected
