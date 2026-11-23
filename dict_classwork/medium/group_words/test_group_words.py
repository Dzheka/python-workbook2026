import threading

import pytest

group_words = pytest.importorskip(
    "group_words", reason="group_words.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(group_words, name, None)
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
    "words, expected",
    [
        (["hi", "cat", "yo", "dog"], {2: ["hi", "yo"], 3: ["cat", "dog"]}),
        ([], {}),
        (["a"], {1: ["a"]}),
        (
            ["sun", "moon", "sky", "star", "a"],
            {3: ["sun", "sky"], 4: ["moon", "star"], 1: ["a"]},
        ),
        (["go", "go"], {2: ["go", "go"]}),
    ],
)
def test_by_length(words, expected):
    assert function("by_length")(words) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["Apple", "bus", "avocado"], {"a": ["Apple", "avocado"], "b": ["bus"]}),
        ([], {}),
        (["Zebra", "zoo", "Zoom"], {"z": ["Zebra", "zoo", "Zoom"]}),
        (["cat", "Dog", "car"], {"c": ["cat", "car"], "d": ["Dog"]}),
    ],
)
def test_by_first_letter(words, expected):
    assert function("by_first_letter")(words) == expected
