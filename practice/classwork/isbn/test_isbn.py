import pytest

isbn = pytest.importorskip("isbn", reason="isbn.py not implemented")


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(isbn, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "code, expected",
    [
        ("0-306-40615-2", "0306406152"),
        ("0 306 40615 2", "0306406152"),
        ("0306406152", "0306406152"),
        ("abc", "abc"),
    ],
)
def test_clean(code, expected):
    assert function("clean")(code) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("0-306-40615-2", True),
        ("0306406152", True),
        ("0-8044-2957-X", True),
        ("0 8044 2957 X", True),
        ("0198526636", True),
        ("0-306-40615-3", False),
        # X is allowed only as the check digit, and only as a capital.
        ("X804429570", False),
        # Passes the checksum if X counted as 10 - but X is not the last character.
        ("03064X6157", False),
        ("0-8044-2957-x", False),
        ("0-306-4061", False),
        ("0-306-4o615-2", False),
        ("", False),
    ],
)
def test_is_valid_isbn10(code, expected):
    assert function("is_valid_isbn10")(code) is expected


@pytest.mark.parametrize(
    "first12, expected",
    [
        ("978030640615", 7),
        ("978080442957", 3),
        ("978019852663", 6),
        ("978000000000", 2),
    ],
)
def test_isbn13_check_digit(first12, expected):
    assert function("isbn13_check_digit")(first12) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("0-306-40615-2", "9780306406157"),
        ("0-8044-2957-X", "9780804429573"),
        ("0198526636", "9780198526636"),
        ("0-306-40615-3", "invalid"),
        ("", "invalid"),
    ],
)
def test_isbn10_to_13(code, expected):
    assert function("isbn10_to_13")(code) == expected
