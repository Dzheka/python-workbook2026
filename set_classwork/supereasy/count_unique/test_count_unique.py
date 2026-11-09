import threading

import pytest

count_unique = pytest.importorskip(
    "count_unique", reason="count_unique.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(count_unique, name, None)
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
        ([3, 1, 3, 2, 1], 3),
        ([], 0),
        ([7, 7, 7], 1),
        (["a", "b", "c"], 3),
        (["Ali", "ali", "Ali"], 2),
    ],
)
def test_count_unique(items, expected):
    assert function("count_unique")(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        (["a", "b", "c"], True),
        (["a", "b", "a"], False),
        ([], True),
        ([5], True),
        ([1, 2, 3, 4, 1], False),
    ],
)
def test_all_different(items, expected):
    assert function("all_different")(items) is expected
