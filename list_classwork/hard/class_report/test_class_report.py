import threading

import pytest

class_report = pytest.importorskip(
    "class_report", reason="class_report.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(class_report, name, None)
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


RECORDS = [["Ali", 85], ["Sara", 92], ["Firuz", 85], ["Madina", 47]]


@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
    ],
)
def test_letter(score, expected):
    assert function("letter")(score) == expected


@pytest.mark.parametrize(
    "records, expected",
    [
        (RECORDS, ["Sara", "Ali", "Firuz", "Madina"]),
        ([["Bo", 70], ["Al", 70], ["Cy", 90]], ["Cy", "Al", "Bo"]),
        ([], []),
        ([["Zed", 50]], ["Zed"]),
    ],
)
def test_ranking(records, expected):
    assert function("ranking")(records) == expected


@pytest.mark.parametrize(
    "records, expected",
    [
        (
            RECORDS,
            "1. Sara - 92 (A)\n2. Ali - 85 (B)\n2. Firuz - 85 (B)\n4. Madina - 47 (F)",
        ),
        ([], ""),
        ([["Zed", 60]], "1. Zed - 60 (D)"),
        (
            [["A", 70], ["B", 70], ["C", 70]],
            "1. A - 70 (C)\n1. B - 70 (C)\n1. C - 70 (C)",
        ),
    ],
)
def test_report(records, expected):
    assert function("report")(records) == expected


@pytest.mark.parametrize(
    "records, expected",
    [
        ([["Ali", 59], ["Sara", 60], ["Bo", 10]], ["Ali", "Bo"]),
        (RECORDS, ["Madina"]),
        ([], []),
    ],
)
def test_failed(records, expected):
    assert function("failed")(records) == expected


def test_input_is_not_changed():
    records = [["Ali", 85], ["Sara", 92]]
    function("ranking")(records)
    function("report")(records)
    assert records == [["Ali", 85], ["Sara", 92]]
