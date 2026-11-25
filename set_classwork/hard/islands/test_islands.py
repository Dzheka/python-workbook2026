import threading

import pytest

islands = pytest.importorskip("islands", reason="islands.py not implemented")

TIME_LIMIT = 5

GRID = [
    "##...",
    "#..#.",
    "...##",
    "#....",
]


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(islands, name, None)
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
    "grid, expected",
    [
        (GRID, 3),
        (["#.#", ".#."], 3),
        (["...", "..."], 0),
        ([], 0),
        (["###", "#.#", "###"], 1),
        (["#.#.#", ".....", "#.#.#"], 6),
        (["##.##", "#...#", "#####"], 1),
    ],
)
def test_count_islands(grid, expected):
    assert function("count_islands")(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (GRID, 3),
        (["...", "..."], 0),
        (["###", "#.#", "###"], 8),
        (["#..", "...", "..#"], 1),
        (["##.##", "#...#", "#####"], 11),
        (["#.##", "#.##", "#..."], 4),
    ],
)
def test_largest_island(grid, expected):
    assert function("largest_island")(grid) == expected
