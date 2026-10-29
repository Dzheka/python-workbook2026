import threading

import pytest

running_stats = pytest.importorskip(
    "running_stats", reason="running_stats.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(running_stats, name, None)
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
    "nums, expected",
    [
        ([3, 1, 4, 1], [3, 4, 8, 9]),
        ([], []),
        ([5], [5]),
        ([2, -2, 2, -2], [2, 0, 2, 0]),
    ],
)
def test_running_sum(nums, expected):
    assert function("running_sum")(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1, 5, 6, 7, 8], 5),
        ([5, 5, 5], 1),
        ([], 0),
        ([7], 1),
        ([9, 8, 7, 6], 1),
        ([1, 2, 3, 4], 4),
        ([1, 3, 2, 4, 6, 1], 3),
    ],
)
def test_longest_growth(nums, expected):
    assert function("longest_growth")(nums) == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 9, 2, 8, 3], 2, 11),
        ([4, -1, 2], 3, 5),
        ([1, 2], 3, 0),
        ([-5, -2, -9], 1, -2),
        ([3, 3, 3, 3], 2, 6),
        ([1, 2, 3, 10], 1, 10),
    ],
)
def test_best_window(nums, k, expected):
    assert function("best_window")(nums, k) == expected


def test_input_is_not_changed():
    nums = [3, 1, 4, 1]
    function("running_sum")(nums)
    assert nums == [3, 1, 4, 1]
