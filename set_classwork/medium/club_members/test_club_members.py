import threading

import pytest

club_members = pytest.importorskip(
    "club_members", reason="club_members.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(club_members, name, None)
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
    "chess, football, expected",
    [
        (["Ali", "Nilu", "Sara"], ["Bek", "Sara", "Ali"], ["Ali", "Sara"]),
        (["Ali"], ["Bek"], []),
        ([], [], []),
        (["Sara", "Sara"], ["Sara"], ["Sara"]),
    ],
)
def test_in_both(chess, football, expected):
    assert function("in_both")(chess, football) == expected


@pytest.mark.parametrize(
    "chess, football, expected",
    [
        (["Ali", "Nilu", "Sara"], ["Bek", "Sara", "Ali"], ["Bek", "Nilu"]),
        (["Ali"], ["Bek"], ["Ali", "Bek"]),
        (["Ali"], ["Ali"], []),
        ([], ["Timur"], ["Timur"]),
    ],
)
def test_in_exactly_one(chess, football, expected):
    assert function("in_exactly_one")(chess, football) == expected


@pytest.mark.parametrize(
    "students, chess, football, expected",
    [
        (
            ["Ali", "Bek", "Madina", "Nilu", "Sara", "Timur"],
            ["Ali", "Nilu", "Sara"],
            ["Bek", "Sara", "Ali"],
            ["Madina", "Timur"],
        ),
        (["Ali", "Bek"], ["Ali"], ["Bek"], []),
        (["Ali", "Bek"], [], [], ["Ali", "Bek"]),
        ([], [], [], []),
    ],
)
def test_in_neither(students, chess, football, expected):
    assert function("in_neither")(students, chess, football) == expected
