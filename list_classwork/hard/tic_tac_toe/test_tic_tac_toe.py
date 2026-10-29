import threading

import pytest

tic_tac_toe = pytest.importorskip(
    "tic_tac_toe", reason="tic_tac_toe.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(tic_tac_toe, name, None)
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
    "board, expected",
    [
        (
            ["XO.", "XO.", "X.."],
            ["XO.", "XO.", "X..", "XXX", "OO.", "...", "XO.", ".OX"],
        ),
        (
            ["ABC", "DEF", "GHI"],
            ["ABC", "DEF", "GHI", "ADG", "BEH", "CFI", "AEI", "CEG"],
        ),
    ],
)
def test_lines(board, expected):
    assert function("lines")(board) == expected


@pytest.mark.parametrize(
    "board, expected",
    [
        (["XO.", "XO.", "X.."], "X"),
        (["...", "...", "..."], ""),
        (["OOO", "XX.", "X.."], "O"),
        (["X.O", ".XO", "..X"], "X"),
        (["X.O", ".OX", "O.X"], "O"),
        (["XOX", "XOO", "OXX"], ""),
    ],
)
def test_winner(board, expected):
    assert function("winner")(board) == expected


@pytest.mark.parametrize(
    "board, expected",
    [
        (["XOX", "XOO", "OXX"], "draw"),
        (["OX.", "XO.", "..O"], "O wins"),
        (["X..", "...", "..."], "in progress"),
        (["XXX", "OO.", "..."], "X wins"),
        (["XOX", "OXO", "OXX"], "X wins"),
        (["...", "...", "..."], "in progress"),
    ],
)
def test_game_state(board, expected):
    assert function("game_state")(board) == expected
