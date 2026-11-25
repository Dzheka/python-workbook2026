import threading

import pytest

common_friends = pytest.importorskip(
    "common_friends", reason="common_friends.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(common_friends, name, None)
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
    "a, b, expected",
    [
        (["Bek", "Nilu", "Timur"], ["Nilu", "Bek"], ["Bek", "Nilu"]),
        (["Bek"], ["Timur"], []),
        ([], ["Timur"], []),
        (["Zara", "Ali", "Ali"], ["Ali", "Zara", "Bek"], ["Ali", "Zara"]),
    ],
)
def test_common(a, b, expected):
    assert function("common")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (["Bek", "Nilu", "Timur"], ["Nilu"], ["Bek", "Timur"]),
        (["Bek"], ["Bek", "Timur"], []),
        (["Timur", "Ali", "Timur"], [], ["Ali", "Timur"]),
        ([], ["Ali"], []),
    ],
)
def test_only_first(a, b, expected):
    assert function("only_first")(a, b) == expected
