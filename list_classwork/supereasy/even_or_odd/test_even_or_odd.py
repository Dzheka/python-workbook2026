import threading

import pytest

even_or_odd = pytest.importorskip(
    "even_or_odd", reason="even_or_odd.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(even_or_odd, name, None)
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
        ([1, 2, 3], ["odd", "even", "odd"]),
        ([], []),
        ([0, 10], ["even", "even"]),
        ([7], ["odd"]),
    ],
)
def test_even_or_odd(nums, expected):
    assert function("even_or_odd")(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 4, 5], 2),
        ([1, 3], 0),
        ([], 0),
        ([0, 0, 0], 3),
    ],
)
def test_count_even(nums, expected):
    assert function("count_even")(nums) == expected
