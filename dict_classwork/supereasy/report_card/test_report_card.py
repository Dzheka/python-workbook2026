import threading

import pytest

report_card = pytest.importorskip(
    "report_card", reason="report_card.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(report_card, name, None)
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


GRADES = {"Ali": 85, "Sara": 92, "Bek": 67, "Nilu": 92}


@pytest.mark.parametrize(
    "grades, expected",
    [
        (GRADES, 84.0),
        ({"Ali": 90, "Bek": 81, "Sara": 80}, 83.7),
        ({"Ali": 50}, 50),
        ({}, 0),
    ],
)
def test_average(grades, expected):
    assert function("average")(grades) == expected


@pytest.mark.parametrize(
    "grades, expected",
    [
        (GRADES, "Nilu"),
        ({"Ali": 70, "Bek": 99}, "Bek"),
        ({"Zara": 5}, "Zara"),
        ({}, None),
    ],
)
def test_best_student(grades, expected):
    assert function("best_student")(grades) == expected


@pytest.mark.parametrize(
    "grades, limit, expected",
    [
        (GRADES, 85, ["Ali", "Nilu", "Sara"]),
        (GRADES, 100, []),
        (GRADES, 0, ["Ali", "Bek", "Nilu", "Sara"]),
        ({}, 50, []),
    ],
)
def test_passed(grades, limit, expected):
    assert function("passed")(grades, limit) == expected
