import threading

import pytest

squares = pytest.importorskip("squares", reason="squares.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(squares, name, None)
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
    "n, expected",
    [
        (4, [1, 4, 9, 16]),
        (1, [1]),
        (0, []),
        (6, [1, 4, 9, 16, 25, 36]),
    ],
)
def test_squares(n, expected):
    assert function("squares")(n) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, 9], 14),
        ([], 0),
        ([5], 5),
        ([-2, 2, 10], 10),
    ],
)
def test_list_sum(nums, expected):
    assert function("list_sum")(nums) == expected
