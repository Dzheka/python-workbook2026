import threading

import pytest

progress_bar = pytest.importorskip(
    "progress_bar", reason="progress_bar.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(progress_bar, name, None)
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
    "percent, width, expected",
    [
        (0, 10, "[----------] 0%"),
        (50, 10, "[#####-----] 50%"),
        (100, 10, "[##########] 100%"),
        (33, 10, "[###-------] 33%"),
        (99, 10, "[#########-] 99%"),
        (75, 4, "[###-] 75%"),
        (120, 10, "[##########] 100%"),
        (-5, 10, "[----------] 0%"),
        (7, 20, "[#-------------------] 7%"),
    ],
)
def test_progress_bar(percent, width, expected):
    assert function("progress_bar")(percent, width) == expected
