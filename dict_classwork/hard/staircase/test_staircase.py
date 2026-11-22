import threading

import pytest

staircase = pytest.importorskip("staircase", reason="staircase.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(staircase, name, None)
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
    "n, steps, expected",
    [
        (0, [1, 2], 1),
        (1, [1, 2], 1),
        (3, [1, 2], 3),
        (4, [1, 2], 5),
        (5, [2], 0),
        (4, [1, 2, 3], 7),
        (10, [3, 5], 1),
        (200, [1, 2], 453973694165307953197296969697410619233826),
        (150, [1, 3, 7], 724900050459573604625483561),
    ],
)
def test_ways(n, steps, expected):
    assert function("ways")(n, steps) == expected


@pytest.mark.parametrize(
    "n, steps, expected",
    [
        (0, [1, 2], 0),
        (7, [1, 3, 5], 3),
        (7, [2, 4], -1),
        (6, [1, 3, 4], 2),
        (11, [5, 2], 4),
        (1000, [7, 13], 82),
    ],
)
def test_min_steps(n, steps, expected):
    assert function("min_steps")(n, steps) == expected
