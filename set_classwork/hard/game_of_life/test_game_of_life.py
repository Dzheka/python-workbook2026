import threading

import pytest

game_of_life = pytest.importorskip(
    "game_of_life", reason="game_of_life.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(game_of_life, name, None)
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
    "cell, expected",
    [
        (
            (0, 0),
            {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)},
        ),
        (
            (5, -2),
            {(4, -3), (4, -2), (4, -1), (5, -3), (5, -1), (6, -3), (6, -2), (6, -1)},
        ),
    ],
)
def test_neighbours(cell, expected):
    assert function("neighbours")(cell) == expected


@pytest.mark.parametrize(
    "live, expected",
    [
        ({(1, 0), (1, 1), (1, 2)}, {(0, 1), (1, 1), (2, 1)}),
        ({(0, 1), (1, 1), (2, 1)}, {(1, 0), (1, 1), (1, 2)}),
        ({(0, 0)}, set()),
        (set(), set()),
        ({(0, 0), (0, 1), (1, 0), (1, 1)}, {(0, 0), (0, 1), (1, 0), (1, 1)}),
        ({(0, 0), (0, 1), (1, 0)}, {(0, 0), (0, 1), (1, 0), (1, 1)}),
        (
            {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)},
            {(1, 0), (1, 2), (2, 1), (2, 2), (3, 1)},
        ),
    ],
)
def test_next_generation(live, expected):
    assert function("next_generation")(live) == expected


@pytest.mark.parametrize(
    "live, steps, expected",
    [
        ({(1, 0), (1, 1), (1, 2)}, 2, {(1, 0), (1, 1), (1, 2)}),
        ({(1, 0), (1, 1), (1, 2)}, 3, {(0, 1), (1, 1), (2, 1)}),
        ({(1, 0), (1, 1), (1, 2)}, 0, {(1, 0), (1, 1), (1, 2)}),
        (
            {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)},
            4,
            {(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)},
        ),
        ({(0, 0), (5, 5)}, 1, set()),
    ],
)
def test_run(live, steps, expected):
    assert function("run")(live, steps) == expected


def test_input_is_not_changed():
    live = {(1, 0), (1, 1), (1, 2)}
    function("next_generation")(live)
    function("run")(live, 3)
    assert live == {(1, 0), (1, 1), (1, 2)}
