import pytest

try:
    from morse_encode import morse_encode
except ImportError:
    morse_encode = None

pytestmark = pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)


def test_sos():
    assert morse_encode("SOS") == "... --- ..."


def test_with_spaces():
    assert morse_encode("HI THERE") == ".... .. / - .... . .-. ."


def test_numbers():
    assert morse_encode("123") == ".---- ..--- ...--"


def test_case_insensitive():
    assert morse_encode("Hello") == morse_encode("HELLO")


def test_empty():
    assert morse_encode("") == ""


def test_single_char():
    assert morse_encode("A") == ".-"


def test_lowercase():
    assert morse_encode("sos") == "... --- ..."


def test_mixed_case():
    assert morse_encode("SoS") == "... --- ..."


def test_alphabet():
    result = morse_encode("ABC")
    assert result == ".- -... -.-."


def test_with_number_and_letter():
    result = morse_encode("A1")
    assert result == ".- .----"
