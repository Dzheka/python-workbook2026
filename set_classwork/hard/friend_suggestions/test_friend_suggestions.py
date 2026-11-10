import threading

import pytest

friend_suggestions = pytest.importorskip(
    "friend_suggestions", reason="friend_suggestions.py not implemented"
)

TIME_LIMIT = 5

PAIRS = [
    ["Ali", "Sara"],
    ["Ali", "Bek"],
    ["Sara", "Nilu"],
    ["Bek", "Nilu"],
    ["Bek", "Timur"],
    ["Nilu", "Madina"],
]


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(friend_suggestions, name, None)
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
    "pairs, name, expected",
    [
        (PAIRS, "Ali", ["Bek", "Sara"]),
        (PAIRS, "Nilu", ["Bek", "Madina", "Sara"]),
        (PAIRS, "Timur", ["Bek"]),
        (PAIRS, "Zara", []),
        ([], "Ali", []),
        ([["Ali", "Sara"], ["Sara", "Ali"]], "Ali", ["Sara"]),
    ],
)
def test_friends_of(pairs, name, expected):
    assert function("friends_of")(pairs, name) == expected


@pytest.mark.parametrize(
    "pairs, name, expected",
    [
        (PAIRS, "Ali", ["Nilu", "Timur"]),
        (PAIRS, "Nilu", ["Ali", "Timur"]),
        (PAIRS, "Madina", ["Bek", "Sara"]),
        (PAIRS, "Timur", ["Ali", "Nilu"]),
        (PAIRS, "Zara", []),
        ([["Ali", "Sara"]], "Ali", []),
        (
            [
                ["A", "B"],
                ["A", "C"],
                ["A", "D"],
                ["B", "X"],
                ["C", "X"],
                ["D", "X"],
                ["B", "Y"],
                ["C", "Y"],
                ["D", "Z"],
            ],
            "A",
            ["X", "Y", "Z"],
        ),
    ],
)
def test_suggestions(pairs, name, expected):
    assert function("suggestions")(pairs, name) == expected


def test_input_is_not_changed():
    pairs = [["Ali", "Sara"], ["Sara", "Bek"]]
    function("suggestions")(pairs, "Ali")
    assert pairs == [["Ali", "Sara"], ["Sara", "Bek"]]
