import threading

import pytest

positives = pytest.importorskip("positives", reason="positives.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(positives, name, None)
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
        ([3, -1, 0, 5], [3, 5]),
        ([-2, -7], []),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_positives(nums, expected):
    assert function("positives")(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, -1], True),
        ([0, 4], False),
        ([], False),
        ([-5], True),
    ],
)
def test_has_negative(nums, expected):
    assert function("has_negative")(nums) is expected
