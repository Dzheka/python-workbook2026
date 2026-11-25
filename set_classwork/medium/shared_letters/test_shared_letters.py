import threading

import pytest

shared_letters = pytest.importorskip(
    "shared_letters", reason="shared_letters.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(shared_letters, name, None)
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
        (["apple", "grape", "pear"], ["a", "e", "p"]),
        (["cat", "dog"], []),
        (["Hello"], ["e", "h", "l", "o"]),
        (["ABC", "cab", "b-a-c!"], ["a", "b", "c"]),
        ([], []),
        (["aa", "a1"], ["a"]),
    ],
)
def test_common_letters(words, expected):
    assert function("common_letters")(words) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["Hi!", "ho"], ["h", "i", "o"]),
        ([], []),
        (["cat", "dog"], ["a", "c", "d", "g", "o", "t"]),
        (["123", "?!"], []),
        (["Aa", "aA"], ["a"]),
    ],
)
def test_any_letters(words, expected):
    assert function("any_letters")(words) == expected
