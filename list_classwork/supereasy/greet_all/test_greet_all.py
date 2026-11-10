import threading

import pytest

greet_all = pytest.importorskip("greet_all", reason="greet_all.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(greet_all, name, None)
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
    "names, expected",
    [
        (["Ali", "Sara"], ["Hello, Ali!", "Hello, Sara!"]),
        ([], []),
        (["Zarina"], ["Hello, Zarina!"]),
    ],
)
def test_greet_all(names, expected):
    assert function("greet_all")(names) == expected


@pytest.mark.parametrize(
    "names, expected",
    [
        (["Ali", "Firuz"], 1),
        (["Ali", "Bob"], 0),
        (["Shahzod", "Madina", "Anna"], 2),
        ([], 0),
    ],
)
def test_count_long_names(names, expected):
    assert function("count_long_names")(names) == expected
