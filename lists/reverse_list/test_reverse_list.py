import pytest

try:
    from reverse_list import reverse_list
except ImportError:
    reverse_list = None

pytestmark = pytest.mark.skipif(
    reverse_list is None, reason="reverse_list function not implemented"
)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", []),
        ("10", [10]),
        ("1 2", [2, 1]),
        ("-5 0 5", [5, 0, -5]),
        ("100 200 300", [300, 200, 100]),
        ("2 3 5 7 11", [11, 7, 5, 3, 2]),
    ],
)
def test_reverse_list(string, expected):
    assert reverse_list(string) == expected
