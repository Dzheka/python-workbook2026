import threading

import pytest

seven_segment = pytest.importorskip(
    "seven_segment", reason="seven_segment.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(seven_segment, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")

    def limited(*args):
        result = {}

        def run():
            try:
                result["value"] = func(*args)
            except Exception as error:  # re-raised below, in the test itself
                result["error"] = error

        worker = threading.Thread(target=run, daemon=True)
        worker.start()
        worker.join(TIME_LIMIT)
        if worker.is_alive():
            pytest.fail(f"{name}{args} did not finish in {TIME_LIMIT}s: endless loop?")
        if "error" in result:
            raise result["error"]
        return result["value"]

    return limited


@pytest.mark.parametrize(
    "digit, row, expected",
    [
        (0, 0, " _ "),
        (0, 1, "| |"),
        (0, 2, "|_|"),
        (1, 0, "   "),
        (1, 2, "  |"),
        (4, 1, "|_|"),
        (7, 1, "  |"),
        (9, 2, " _|"),
    ],
)
def test_digit_row(digit, row, expected):
    assert function("digit_row")(digit, row) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (8, " _ \n|_|\n|_|"),
        (1, "   \n  |\n  |"),
        (42, "    _ \n|_| _|\n  ||_ "),
        (2026, " _  _  _  _ \n _|| | _||_ \n|_ |_||_ |_|"),
        (
            1234567890,
            "    _  _     _  _  _  _  _  _ \n  | _| _||_||_ |_   ||_||_|| |\n  ||_  _|  | _||_|  ||_| _||_|",
        ),
    ],
)
def test_render(number, expected):
    assert function("render")(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (8, 7),
        (1, 2),
        (0, 6),
        (7, 3),
        (2026, 22),
        (1234567890, 49),
    ],
)
def test_segment_count(number, expected):
    assert function("segment_count")(number) == expected
