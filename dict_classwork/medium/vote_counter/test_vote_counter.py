import threading

import pytest

vote_counter = pytest.importorskip(
    "vote_counter", reason="vote_counter.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(vote_counter, name, None)
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


VOTES = ["Sara", "Ali", "Sara", "Bek", "Ali", "Sara"]


@pytest.mark.parametrize(
    "votes, expected",
    [
        (VOTES, {"Sara": 3, "Ali": 2, "Bek": 1}),
        ([], {}),
        (["Ali"], {"Ali": 1}),
    ],
)
def test_tally(votes, expected):
    assert function("tally")(votes) == expected


@pytest.mark.parametrize(
    "votes, expected",
    [
        (VOTES, "Sara"),
        (["Bek", "Ali"], "Ali"),
        (["Timur", "Nilu", "Timur", "Nilu", "Ali"], "Nilu"),
        (["Zara"], "Zara"),
        ([], None),
    ],
)
def test_winner(votes, expected):
    assert function("winner")(votes) == expected


@pytest.mark.parametrize(
    "votes, expected",
    [
        (VOTES, {"Sara": 50.0, "Ali": 33.3, "Bek": 16.7}),
        (["Ali", "Ali"], {"Ali": 100.0}),
        (["A", "B", "C"], {"A": 33.3, "B": 33.3, "C": 33.3}),
        ([], {}),
    ],
)
def test_percentages(votes, expected):
    assert function("percentages")(votes) == expected
