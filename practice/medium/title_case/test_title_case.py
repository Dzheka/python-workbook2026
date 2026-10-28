import inspect
import threading

import pytest

title_case = pytest.importorskip("title_case", reason="title_case.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(title_case, name, None)
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


def test_no_ready_made_methods():
    source = inspect.getsource(title_case)
    for method in (".title(", ".capitalize(", ".split("):
        assert method not in source, (
            f"Do it letter by letter: {method[1:-1]}() is not allowed here."
        )


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "Hello World"),
        ("HELLO WORLD", "Hello World"),
        ("pYTHON", "Python"),
        ("", ""),
        ("  two  spaces ", "  Two  Spaces "),
        ("a b c", "A B C"),
    ],
)
def test_to_title(text, expected):
    assert function("to_title")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 2),
        ("", 0),
        ("   ", 0),
        ("  two  spaces ", 2),
        ("one", 1),
    ],
)
def test_count_words(text, expected):
    assert function("count_words")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("John Ronald Reuel Tolkien", "J.R.R.T."),
        ("ada lovelace", "A.L."),
        ("", ""),
        ("  guido   van rossum ", "G.V.R."),
    ],
)
def test_initials(text, expected):
    assert function("initials")(text) == expected
