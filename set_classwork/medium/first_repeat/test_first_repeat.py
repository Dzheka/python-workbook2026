import threading

import pytest

first_repeat = pytest.importorskip(
    "first_repeat", reason="first_repeat.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(first_repeat, name, None)
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
    "items, expected",
    [
        (["red", "blue", "green", "blue", "red"], "blue"),
        ([1, 2, 3], None),
        ([], None),
        ([5, 5], 5),
        ([1, 2, 3, 4, 3, 2, 1], 3),
    ],
)
def test_first_repeat(items, expected):
    assert function("first_repeat")(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([3, 1, 3, 2, 1], [3, 1, 2]),
        ([], []),
        (["b", "a", "b", "a"], ["b", "a"]),
        ([9, 8, 7], [9, 8, 7]),
        ([0, 0, 0], [0]),
    ],
)
def test_remove_repeats(items, expected):
    assert function("remove_repeats")(items) == expected


def test_none_when_no_repeat():
    assert function("first_repeat")(["a", "b"]) is None


def test_input_is_not_changed():
    items = [3, 1, 3, 2, 1]
    function("first_repeat")(items)
    function("remove_repeats")(items)
    assert items == [3, 1, 3, 2, 1]
