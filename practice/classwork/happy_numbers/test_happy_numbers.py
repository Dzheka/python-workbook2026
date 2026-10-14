import pytest

happy_numbers = pytest.importorskip(
    "happy_numbers", reason="happy_numbers.py not implemented"
)


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(happy_numbers, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (7, 49), (19, 82), (82, 68), (999, 243), (1000, 1)],
)
def test_square_digit_sum(n, expected):
    assert function("square_digit_sum")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (7, True),
        (19, True),
        (100, True),
        (986543210, True),
        (2, False),
        (4, False),
        (20, False),
    ],
)
def test_is_happy(n, expected):
    assert function("is_happy")(n) is expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 10, 3),
        (1, 100, 20),
        (11, 12, 0),
        (50, 60, 0),
        # Both ends are included.
        (7, 7, 1),
        (1, 1000, 143),
    ],
)
def test_count_happy(start, end, expected):
    assert function("count_happy")(start, end) == expected


@pytest.mark.parametrize(
    "k, expected",
    [(1, 1), (2, 7), (5, 19), (10, 44), (20, 100), (143, 1000)],
)
def test_nth_happy(k, expected):
    assert function("nth_happy")(k) == expected
