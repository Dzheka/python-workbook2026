import threading

import pytest

sudoku_check = pytest.importorskip(
    "sudoku_check", reason="sudoku_check.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(sudoku_check, name, None)
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


SOLVED = (
    "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
)


@pytest.mark.parametrize(
    "grid, row, col, expected",
    [
        (SOLVED, 0, 0, "5"),
        (SOLVED, 1, 0, "6"),
        (SOLVED, 0, 8, "2"),
        (SOLVED, 4, 4, "5"),
        (SOLVED, 8, 8, "9"),
    ],
)
def test_cell(grid, row, col, expected):
    assert function("cell")(grid, row, col) == expected


@pytest.mark.parametrize(
    "grid, row, expected",
    [
        (SOLVED, 0, True),
        (SOLVED, 8, True),
        (
            "634678912572195348198342567859761423426853791713924856961537284287419635345286179",
            0,
            False,
        ),
        (
            "634678912572195348198342567859761423426853791713924856961537284287419635345286179",
            2,
            True,
        ),
        (
            "123456789234567891345678912456789123567891234678912345789123456891234567912345678",
            4,
            True,
        ),
    ],
)
def test_row_ok(grid, row, expected):
    assert function("row_ok")(grid, row) is expected


@pytest.mark.parametrize(
    "grid, col, expected",
    [
        (SOLVED, 0, True),
        (SOLVED, 8, True),
        (
            "354678912672195348198342567859761423426853791713924856961537284287419635345286179",
            0,
            False,
        ),
        (
            "354678912672195348198342567859761423426853791713924856961537284287419635345286179",
            5,
            True,
        ),
        (
            "123456789234567891345678912456789123567891234678912345789123456891234567912345678",
            4,
            True,
        ),
    ],
)
def test_col_ok(grid, col, expected):
    assert function("col_ok")(grid, col) is expected


@pytest.mark.parametrize(
    "grid, box, expected",
    [
        (SOLVED, 0, True),
        (SOLVED, 4, True),
        (SOLVED, 8, True),
        (
            "634578912672195348198342567859761423426853791713924856961537284287419635345286179",
            0,
            False,
        ),
        (
            "634578912672195348198342567859761423426853791713924856961537284287419635345286179",
            1,
            False,
        ),
        (
            "634578912672195348198342567859761423426853791713924856961537284287419635345286179",
            2,
            True,
        ),
        (
            "634578912672195348198342567859761423426853791713924856961537284287419635345286179",
            3,
            True,
        ),
        (
            "123456789234567891345678912456789123567891234678912345789123456891234567912345678",
            0,
            False,
        ),
    ],
)
def test_box_ok(grid, box, expected):
    assert function("box_ok")(grid, box) is expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (SOLVED, True),
        (
            "634678912572195348198342567859761423426853791713924856961537284287419635345286179",
            False,
        ),
        (
            "354678912672195348198342567859761423426853791713924856961537284287419635345286179",
            False,
        ),
        (
            "53467891267219534819834256785976142342685379171392485696153728428741963534528617",
            False,
        ),
        (
            "534678912672195348198342567859761423426853791713924856961537284287419635345286170",
            False,
        ),
        (
            "123456789123456789123456789123456789123456789123456789123456789123456789123456789",
            False,
        ),
        (
            "123456789234567891345678912456789123567891234678912345789123456891234567912345678",
            False,
        ),
    ],
)
def test_is_solved(grid, expected):
    assert function("is_solved")(grid) is expected
