import threading

import pytest

top_words = pytest.importorskip("top_words", reason="top_words.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(top_words, name, None)
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


TEXT = "The dog saw the cat. The cat ran! A dog?"


@pytest.mark.parametrize(
    "text, k, expected",
    [
        (TEXT, 3, [("the", 3), ("cat", 2), ("dog", 2)]),
        (TEXT, 1, [("the", 3)]),
        (
            TEXT,
            100,
            [("the", 3), ("cat", 2), ("dog", 2), ("a", 1), ("ran", 1), ("saw", 1)],
        ),
        ("", 2, []),
        ("Hi! hi? HI.", 2, [("hi", 3)]),
        ("b a c b a", 2, [("a", 2), ("b", 2)]),
        ("one two", 0, []),
    ],
)
def test_top_words(text, k, expected):
    assert function("top_words")(text, k) == expected
