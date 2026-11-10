import pytest

try:
    from morse_decode import morse_decode
except ImportError:
    morse_decode = None

pytestmark = pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)


def test_sos():
    assert morse_decode("... --- ...") == "SOS"


def test_with_words():
    assert morse_decode(".... .. / - .... . .-. .") == "HI THERE"


def test_numbers():
    assert morse_decode(".---- ..--- ...--") == "123"


def test_empty():
    assert morse_decode("") == ""


def test_single_letter():
    assert morse_decode(".-") == "A"


def test_hello():
    assert morse_decode(".... . .-.. .-.. ---") == "HELLO"


def test_alphabet():
    assert morse_decode(".- -... -.-.") == "ABC"


def test_mixed():
    assert morse_decode(".- .----") == "A1"
