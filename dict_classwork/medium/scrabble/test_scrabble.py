import threading

import pytest

scrabble = pytest.importorskip("scrabble", reason="scrabble.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(scrabble, name, None)
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


def test_scores_table():
    scores = getattr(scrabble, "SCORES", None)
    if scores is None:
        pytest.skip("SCORES not defined")
    assert len(scores) == 26
    assert scores["a"] == 1
    assert scores["g"] == 2
    assert scores["m"] == 3
    assert scores["y"] == 4
    assert scores["k"] == 5
    assert scores["x"] == 8
    assert scores["q"] == 10


@pytest.mark.parametrize(
    "word, expected",
    [
        ("cab", 7),
        ("Quiz", 22),
        ("", 0),
        ("CAB", 7),
        ("oxyphenbutazone", 41),
        ("e-mail 2", 7),
    ],
)
def test_word_score(word, expected):
    assert function("word_score")(word) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["cat", "dog", "zoo"], "zoo"),
        (["at", "ta"], "at"),
        (["jazz"], "jazz"),
        (["hi", "Kiwi", "fox"], "fox"),
        ([], None),
    ],
)
def test_best_word(words, expected):
    assert function("best_word")(words) == expected
