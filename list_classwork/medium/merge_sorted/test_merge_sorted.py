import threading

import pytest

merge_sorted = pytest.importorskip(
    "merge_sorted", reason="merge_sorted.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(merge_sorted, name, None)
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
        ([1, 4, 9], [2, 3, 10], [1, 2, 3, 4, 9, 10]),
        ([], [5, 6], [5, 6]),
        ([5, 6], [], [5, 6]),
        ([], [], []),
        ([1, 2], [2, 2], [1, 2, 2, 2]),
        ([-3, 0], [-5, 8, 9], [-5, -3, 0, 8, 9]),
    ],
)
def test_merge(a, b, expected):
    assert function("merge")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 2, 5, 7], [2, 2, 3, 7], [2, 7]),
        ([1, 3], [2, 4], []),
        ([], [1], []),
        ([4, 4, 4], [4], [4]),
    ],
)
def test_common(a, b, expected):
    assert function("common")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 2, 5], [2, 3], [1, 5]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 2], [1, 2], []),
        ([3, 3, 4], [1], [3, 4]),
    ],
)
def test_only_in_first(a, b, expected):
    assert function("only_in_first")(a, b) == expected


def test_merge_does_not_change_input():
    a, b = [1, 3], [2]
    function("merge")(a, b)
    assert (a, b) == ([1, 3], [2])
