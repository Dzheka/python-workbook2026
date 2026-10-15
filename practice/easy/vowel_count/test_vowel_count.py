import threading

import pytest

vowel_count = pytest.importorskip(
    "vowel_count", reason="vowel_count.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(vowel_count, name, None)
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
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
        ("Python Is Fun!", 3),
    ],
)
def test_count_vowels(text, expected):
    assert function("count_vowels")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 3),
        ("AEIOU", 0),
        ("rhythm", 6),
        ("", 0),
        ("Python Is Fun!", 8),
        ("a1 b2", 1),
    ],
)
def test_count_consonants(text, expected):
    assert function("count_consonants")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("audio", True),
        ("hello", False),
        ("idea", True),
        ("", False),
        ("Aa b", True),
    ],
)
def test_more_vowels(text, expected):
    assert function("more_vowels")(text) is expected
