import pytest

bulls_and_cows = pytest.importorskip(
    "bulls_and_cows", reason="bulls_and_cows.py not implemented"
)


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(bulls_and_cows, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "code, expected",
    [
        ("1234", True),
        ("9876", True),
        ("1023", True),
        ("0123", False),
        ("1123", False),
        # The repeated digits are not next to each other.
        ("1231", False),
        ("123", False),
        ("12345", False),
        ("12a4", False),
    ],
)
def test_is_valid_secret(code, expected):
    assert function("is_valid_secret")(code) is expected


@pytest.mark.parametrize(
    "secret, guess, expected",
    [("1234", "1243", 2), ("1234", "5678", 0), ("1234", "1234", 4)],
)
def test_bulls(secret, guess, expected):
    assert function("bulls")(secret, guess) == expected


@pytest.mark.parametrize(
    "secret, guess, expected",
    [
        ("1234", "1243", 2),
        ("1234", "4321", 4),
        ("1234", "5678", 0),
        # A bull is never a cow as well.
        ("1234", "1234", 0),
    ],
)
def test_cows(secret, guess, expected):
    assert function("cows")(secret, guess) == expected


@pytest.mark.parametrize(
    "secret, guess, expected",
    [
        ("1234", "1243", "2B2C"),
        ("5823", "5381", "1B2C"),
        ("1234", "5678", "0B0C"),
        ("1234", "4321", "0B4C"),
        ("7012", "7019", "3B0C"),
        ("1234", "1234", "win"),
        ("1234", "1123", "invalid"),
        ("1234", "0123", "invalid"),
        ("1234", "123", "invalid"),
    ],
)
def test_score(secret, guess, expected):
    assert function("score")(secret, guess) == expected
