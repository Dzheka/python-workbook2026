import threading

import pytest

taxi_fare = pytest.importorskip("taxi_fare", reason="taxi_fare.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(taxi_fare, name, None)
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
    "km, night, expected",
    [
        (0, False, 5.0),
        (4, False, 13.0),
        (10, False, 25.0),
        (14, False, 31.0),
        (14, True, 38.75),
        (2.5, True, 12.5),
        (25, False, 47.5),
        (0, True, 6.25),
    ],
)
def test_fare(km, night, expected):
    assert function("fare")(km, night) == pytest.approx(expected, abs=0.01)
