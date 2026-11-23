import threading

import pytest

phone_book = pytest.importorskip("phone_book", reason="phone_book.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(phone_book, name, None)
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


BOOK = {"Ali": "901-11-22", "Sara": "933-44-55", "Bek": "918-00-01"}


@pytest.mark.parametrize(
    "book, name, expected",
    [
        (BOOK, "Sara", "933-44-55"),
        (BOOK, "Ali", "901-11-22"),
        (BOOK, "Timur", "not found"),
        (BOOK, "ali", "not found"),
        ({}, "Ali", "not found"),
    ],
)
def test_lookup(book, name, expected):
    assert function("lookup")(book, name) == expected


@pytest.mark.parametrize(
    "book, expected",
    [
        (BOOK, ["Ali", "Bek", "Sara"]),
        ({"Zara": "1"}, ["Zara"]),
        ({}, []),
    ],
)
def test_names(book, expected):
    assert function("names")(book) == expected


@pytest.mark.parametrize(
    "book, number, expected",
    [
        (BOOK, "918-00-01", True),
        (BOOK, "933-44-55", True),
        (BOOK, "000-00-00", False),
        (BOOK, "Ali", False),
        ({}, "901-11-22", False),
    ],
)
def test_has_number(book, number, expected):
    assert function("has_number")(book, number) == expected
