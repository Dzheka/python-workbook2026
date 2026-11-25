import threading

import pytest

spell_checker = pytest.importorskip(
    "spell_checker", reason="spell_checker.py not implemented"
)

TIME_LIMIT = 5

DICTIONARY = ["hello", "help", "halo", "held", "world", "word", "a", "the"]


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(spell_checker, name, None)
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
    "text, dictionary, expected",
    [
        ("Helo wrld, the helo!", DICTIONARY, ["helo", "wrld"]),
        ("hello world", DICTIONARY, []),
        ("", DICTIONARY, []),
        ("Wrd? wrd. WRD!", DICTIONARY, ["wrd"]),
        ("the cat, a dog", DICTIONARY, ["cat", "dog"]),
        ("hello", [], ["hello"]),
    ],
)
def test_unknown_words(text, dictionary, expected):
    assert function("unknown_words")(text, dictionary) == expected


@pytest.mark.parametrize(
    "word, dictionary, expected",
    [
        ("helo", DICTIONARY, ["halo", "held", "hello", "help"]),
        ("wrld", DICTIONARY, ["world"]),
        ("xyz", DICTIONARY, []),
        ("hello", DICTIONARY, []),
        ("wordd", DICTIONARY, ["word", "world"]),
        ("", DICTIONARY, ["a"]),
        ("ahe", DICTIONARY, ["the"]),
        ("wod", DICTIONARY, ["word"]),
    ],
)
def test_suggest(word, dictionary, expected):
    assert function("suggest")(word, dictionary) == expected
