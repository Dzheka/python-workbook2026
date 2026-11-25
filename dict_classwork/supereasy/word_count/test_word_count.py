import threading

import pytest

word_count = pytest.importorskip("word_count", reason="word_count.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(word_count, name, None)
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
    "text, expected",
    [
        ("the cat and the dog", {"the": 2, "cat": 1, "and": 1, "dog": 1}),
        ("Go go GO", {"go": 3}),
        ("", {}),
        ("one", {"one": 1}),
        ("a  b   a", {"a": 2, "b": 1}),
    ],
)
def test_count_words(text, expected):
    assert function("count_words")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("the cat and the dog", ["and", "cat", "dog"]),
        ("Go go GO", []),
        ("", []),
        ("b a C a", ["b", "c"]),
    ],
)
def test_unique_words(text, expected):
    assert function("unique_words")(text) == expected
