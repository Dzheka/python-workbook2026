import threading

import pytest

text_similarity = pytest.importorskip(
    "text_similarity", reason="text_similarity.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(text_similarity, name, None)
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
    "text1, text2, expected",
    [
        ("the cat sat", "the cat ran", 0.5),
        ("I like tea", "tea I like", 1.0),
        ("red", "blue", 0.0),
        ("", "", 1.0),
        ("a a a b", "b c", 0.33),
        ("Hello World", "hello world again", 0.67),
        ("", "word", 0.0),
    ],
)
def test_similarity(text1, text2, expected):
    assert function("similarity")(text1, text2) == expected


@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("the cat sat", "The dog SAT", ["cat"]),
        ("one two", "", ["one", "two"]),
        ("", "one", []),
        ("b a b a", "c", ["a", "b"]),
    ],
)
def test_unique_to_first(text1, text2, expected):
    assert function("unique_to_first")(text1, text2) == expected
