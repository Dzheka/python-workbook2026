import threading

import pytest

flip_dict = pytest.importorskip("flip_dict", reason="flip_dict.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(flip_dict, name, None)
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
    "d, expected",
    [
        ({"one": 1, "two": 2}, {1: "one", 2: "two"}),
        ({"red": "#f00", "blue": "#00f"}, {"#f00": "red", "#00f": "blue"}),
        ({}, {}),
        ({"a": "b", "b": "a"}, {"b": "a", "a": "b"}),
    ],
)
def test_invert(d, expected):
    assert function("invert")(d) == expected


def test_invert_does_not_change_input():
    d = {"one": 1, "two": 2}
    function("invert")(d)
    assert d == {"one": 1, "two": 2}


@pytest.mark.parametrize(
    "d, value, expected",
    [
        ({"Ali": "A", "Bek": "B", "Sara": "A"}, "A", ["Ali", "Sara"]),
        ({"Ali": "A"}, "C", []),
        ({"x": 0, "y": 0, "a": 0}, 0, ["a", "x", "y"]),
        ({}, 1, []),
    ],
)
def test_keys_for(d, value, expected):
    assert function("keys_for")(d, value) == expected
