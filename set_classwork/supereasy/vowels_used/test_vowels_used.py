import threading

import pytest

vowels_used = pytest.importorskip(
    "vowels_used", reason="vowels_used.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(vowels_used, name, None)
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
    "word, expected",
    [
        ("banana", ["a"]),
        ("Education", ["a", "e", "i", "o", "u"]),
        ("rhythm", []),
        ("", []),
        ("OOPS", ["o"]),
    ],
)
def test_vowels_in(word, expected):
    assert function("vowels_in")(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("hello", ["a", "i", "u"]),
        ("rhythm", ["a", "e", "i", "o", "u"]),
        ("sequoia", []),
        ("APPLE", ["i", "o", "u"]),
    ],
)
def test_missing_vowels(word, expected):
    assert function("missing_vowels")(word) == expected
