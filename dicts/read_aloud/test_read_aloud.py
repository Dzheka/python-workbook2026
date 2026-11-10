import pytest

try:
    from read_aloud import read_aloud
except ImportError:
    read_aloud = None

pytestmark = pytest.mark.skipif(
    read_aloud is None, reason="read_aloud function not implemented"
)


def test_basic():
    assert read_aloud("42") == "FORTY TWO"


def test_single_digit():
    assert read_aloud("7") == "SEVEN"


def test_with_zero():
    assert read_aloud("105") == "ONE HUNDRED FIVE"


def test_all_same():
    assert read_aloud("333") == "THREE HUNDRED THIRTY THREE"


def test_empty():
    assert read_aloud("") == ""


def test_long_number():
    result = read_aloud("123")
    assert result == "ONE HUNDRED TWENTY THREE"


def test_all_zeros():
    assert read_aloud("0") == "ZERO"


def test_teens():
    assert read_aloud("15") == "FIFTEEN"
    assert read_aloud("10") == "TEN"
    assert read_aloud("19") == "NINETEEN"


def test_tens():
    assert read_aloud("20") == "TWENTY"
    assert read_aloud("50") == "FIFTY"
    assert read_aloud("90") == "NINETY"


def test_hundreds():
    assert read_aloud("100") == "ONE HUNDRED"
    assert read_aloud("200") == "TWO HUNDRED"
    assert read_aloud("500") == "FIVE HUNDRED"
