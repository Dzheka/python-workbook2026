import pytest

try:
    from is_triangle import is_triangle
except ImportError:
    is_triangle = None

pytestmark = pytest.mark.skipif(
    is_triangle is None, reason="is_triangle function not implemented"
)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (1, 2, 3, False),
        (5, 5, 5, True),
        (1, 1, 10, False),
        (7, 10, 5, True),
        (0, 1, 1, False),
        (-1, 2, 3, False),
        (10, 10, 1, True),
        (1, 2, 10, False),
    ],
)
def test_is_triangle(a, b, c, expected):
    assert is_triangle(a, b, c) == expected
