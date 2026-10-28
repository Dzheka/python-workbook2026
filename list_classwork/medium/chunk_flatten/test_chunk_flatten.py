import threading

import pytest

chunk_flatten = pytest.importorskip(
    "chunk_flatten", reason="chunk_flatten.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(chunk_flatten, name, None)
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
    "items, size, expected",
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3], 5, [[1, 2, 3]]),
        ([], 2, []),
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
        (["a", "b", "c"], 1, [["a"], ["b"], ["c"]]),
    ],
)
def test_chunk(items, size, expected):
    assert function("chunk")(items, size) == expected


@pytest.mark.parametrize(
    "nested, expected",
    [
        ([[1, 2], [], [3]], [1, 2, 3]),
        ([], []),
        ([[], []], []),
        ([["a"], ["b", "c"]], ["a", "b", "c"]),
        ([[1, [2]], [3]], [1, [2], 3]),
    ],
)
def test_flatten(nested, expected):
    assert function("flatten")(nested) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], ["a", "b"], [1, "a", 2, "b", 3]),
        ([], [7, 8], [7, 8]),
        ([7, 8], [], [7, 8]),
        ([1], [2, 3, 4], [1, 2, 3, 4]),
        ([], [], []),
    ],
)
def test_interleave(a, b, expected):
    assert function("interleave")(a, b) == expected


def test_flatten_undoes_chunk():
    items = list(range(11))
    assert function("flatten")(function("chunk")(items, 3)) == items
