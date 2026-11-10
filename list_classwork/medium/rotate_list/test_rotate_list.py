import threading

import pytest

rotate_list = pytest.importorskip(
    "rotate_list", reason="rotate_list.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(rotate_list, name, None)
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
    "items, k, expected",
    [
        ([1, 2, 3, 4], 1, [2, 3, 4, 1]),
        ([1, 2, 3, 4], 0, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 6, [3, 4, 1, 2]),
        ([], 3, []),
        (["a"], 5, ["a"]),
    ],
)
def test_rotate_left(items, k, expected):
    assert function("rotate_left")(items, k) == expected


@pytest.mark.parametrize(
    "items, k, expected",
    [
        ([1, 2, 3, 4], 1, [4, 1, 2, 3]),
        ([1, 2, 3, 4], 3, [2, 3, 4, 1]),
        ([1, 2, 3, 4], 9, [4, 1, 2, 3]),
        ([], 3, []),
        ([1, 2], 0, [1, 2]),
    ],
)
def test_rotate_right(items, k, expected):
    assert function("rotate_right")(items, k) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [3, 1, 2], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 3], [1, 3, 2], False),
        ([1, 2, 3], [1, 2], False),
        ([], [], True),
        ([1, 1, 2], [1, 2, 1], True),
        ([1, 1, 2], [2, 2, 1], False),
    ],
)
def test_is_rotation(a, b, expected):
    assert function("is_rotation")(a, b) is expected


def test_input_is_not_changed():
    items = [1, 2, 3, 4]
    function("rotate_left")(items, 1)
    function("rotate_right")(items, 1)
    assert items == [1, 2, 3, 4]
