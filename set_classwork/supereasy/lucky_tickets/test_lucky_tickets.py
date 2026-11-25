import threading

import pytest

lucky_tickets = pytest.importorskip(
    "lucky_tickets", reason="lucky_tickets.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(lucky_tickets, name, None)
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
    "tickets, winners, expected",
    [
        ([12, 7, 30, 7], [7, 30, 41], [7, 30]),
        ([1, 2], [3], []),
        ([], [3], []),
        ([50, 40, 30], [30, 40, 50], [30, 40, 50]),
    ],
)
def test_winning(tickets, winners, expected):
    assert function("winning")(tickets, winners) == expected


@pytest.mark.parametrize(
    "tickets, winners, expected",
    [
        ([1, 2], [2, 5], True),
        ([1, 2], [], False),
        ([], [1], False),
        ([9, 8, 7], [1, 2, 3], False),
        ([9, 8, 7], [7], True),
    ],
)
def test_has_winner(tickets, winners, expected):
    assert function("has_winner")(tickets, winners) is expected
