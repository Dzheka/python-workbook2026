import threading

import pytest

league_table = pytest.importorskip(
    "league_table", reason="league_table.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(league_table, name, None)
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


MATCHES = [
    ("Istiklol", 2, 1, "Khujand"),
    ("Ravshan", 0, 0, "Istiklol"),
    ("Khujand", 3, 0, "Ravshan"),
    ("Istiklol", 1, 2, "Ravshan"),
]


@pytest.mark.parametrize(
    "matches, expected",
    [
        (
            MATCHES,
            [
                ("Istiklol", 3, 4, 0),
                ("Ravshan", 3, 4, -2),
                ("Khujand", 2, 3, 2),
            ],
        ),
        ([], []),
        ([("B", 1, 1, "A")], [("A", 1, 1, 0), ("B", 1, 1, 0)]),
        ([("A", 0, 3, "B")], [("B", 1, 3, 3), ("A", 1, 0, -3)]),
        (
            [("A", 1, 0, "B"), ("B", 1, 0, "C"), ("C", 1, 0, "A")],
            [("A", 2, 3, 0), ("B", 2, 3, 0), ("C", 2, 3, 0)],
        ),
        (
            [("A", 5, 0, "C"), ("B", 1, 0, "C"), ("A", 0, 0, "B")],
            [("A", 2, 4, 5), ("B", 2, 4, 1), ("C", 2, 0, -6)],
        ),
    ],
)
def test_standings(matches, expected):
    assert function("standings")(matches) == expected


@pytest.mark.parametrize(
    "matches, expected",
    [
        (MATCHES, "Istiklol"),
        ([], None),
        ([("B", 1, 1, "A")], "A"),
        ([("A", 0, 1, "B")], "B"),
    ],
)
def test_leader(matches, expected):
    assert function("leader")(matches) == expected
