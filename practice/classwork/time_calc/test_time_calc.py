import pytest

time_calc = pytest.importorskip("time_calc", reason="time_calc.py not implemented")


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(time_calc, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "time, expected",
    [
        ("00:00", True),
        ("23:59", True),
        ("09:05", True),
        ("24:00", False),
        ("12:60", False),
        ("7:30", False),
        ("07:300", False),
        ("12-30", False),
        ("ab:cd", False),
        ("", False),
    ],
)
def test_is_valid_time(time, expected):
    assert function("is_valid_time")(time) is expected


@pytest.mark.parametrize(
    "time, expected",
    [("00:00", 0), ("00:01", 1), ("13:45", 825), ("23:59", 1439)],
)
def test_to_minutes(time, expected):
    assert function("to_minutes")(time) == expected


@pytest.mark.parametrize(
    "time, minutes, expected",
    [
        ("09:05", 0, "09:05"),
        ("10:20", 45, "11:05"),
        ("23:45", 30, "00:15"),
        ("00:10", -20, "23:50"),
        ("12:00", 1440, "12:00"),
        ("08:15", 3000, "10:15"),
        # More than a day backwards.
        ("06:30", -1500, "05:30"),
    ],
)
def test_add_minutes(time, minutes, expected):
    assert function("add_minutes")(time, minutes) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ("09:00", "17:30", 510),
        ("23:30", "01:15", 105),
        ("12:00", "12:00", 0),
        ("00:01", "00:00", 1439),
    ],
)
def test_duration(start, end, expected):
    assert function("duration")(start, end) == expected


@pytest.mark.parametrize(
    "time, expected",
    [
        ("00:00", "12:00 AM"),
        ("00:15", "12:15 AM"),
        ("09:30", "9:30 AM"),
        ("11:59", "11:59 AM"),
        ("12:00", "12:00 PM"),
        ("13:05", "1:05 PM"),
        ("23:59", "11:59 PM"),
    ],
)
def test_to_12h(time, expected):
    assert function("to_12h")(time) == expected
