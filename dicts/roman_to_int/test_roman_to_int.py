import pytest

try:
    from roman_to_int import roman_to_int
except ImportError:
    roman_to_int = None

pytestmark = pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)


def test_basic_iii():
    assert roman_to_int("III") == 3


def test_subtraction_iv():
    assert roman_to_int("IV") == 4


def test_subtraction_ix():
    assert roman_to_int("IX") == 9


def test_complex_mcmxciv():
    assert roman_to_int("MCMXCIV") == 1994


def test_lviii():
    assert roman_to_int("LVIII") == 58


def test_single_i():
    assert roman_to_int("I") == 1


def test_xiv():
    assert roman_to_int("XIV") == 14


def test_xl():
    assert roman_to_int("XL") == 40


def test_cd():
    assert roman_to_int("CD") == 400


def test_cm():
    assert roman_to_int("CM") == 900


def test_large_mmmcmxcix():
    assert roman_to_int("MMMCMXCIX") == 3999


def test_xcix():
    assert roman_to_int("XCIX") == 99
