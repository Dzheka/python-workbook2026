import threading

import pytest

flight_routes = pytest.importorskip(
    "flight_routes", reason="flight_routes.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(flight_routes, name, None)
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


FLIGHTS = [
    ["Dushanbe", "Moscow"],
    ["Dushanbe", "Istanbul"],
    ["Moscow", "Berlin"],
    ["Istanbul", "Berlin"],
    ["Berlin", "London"],
    ["London", "Dushanbe"],
    ["Khujand", "Moscow"],
]

CHAIN = [[str(i), str(i + 1)] for i in range(2000)]


@pytest.mark.parametrize(
    "flights, city, expected",
    [
        (FLIGHTS, "Dushanbe", ["Istanbul", "Moscow"]),
        (FLIGHTS, "Berlin", ["London"]),
        (FLIGHTS, "Paris", []),
        ([["A", "B"], ["A", "B"]], "A", ["B"]),
        ([], "A", []),
    ],
)
def test_direct(flights, city, expected):
    assert function("direct")(flights, city) == expected


@pytest.mark.parametrize(
    "flights, start, expected",
    [
        (FLIGHTS, "Khujand", ["Berlin", "Dushanbe", "Istanbul", "London", "Moscow"]),
        (FLIGHTS, "Dushanbe", ["Berlin", "Istanbul", "London", "Moscow"]),
        ([["A", "B"], ["C", "A"]], "A", ["B"]),
        ([["A", "A"]], "A", []),
        ([], "A", []),
    ],
)
def test_reachable(flights, start, expected):
    assert function("reachable")(flights, start) == expected


@pytest.mark.parametrize(
    "flights, start, end, expected",
    [
        (FLIGHTS, "Dushanbe", "London", 3),
        (FLIGHTS, "Berlin", "Khujand", -1),
        (FLIGHTS, "Khujand", "Istanbul", 5),
        (FLIGHTS, "London", "London", 0),
        ([["A", "B"], ["B", "C"], ["A", "C"]], "A", "C", 1),
        ([["B", "A"]], "A", "B", -1),
        (CHAIN, "0", "2000", 2000),
    ],
)
def test_fewest_flights(flights, start, end, expected):
    assert function("fewest_flights")(flights, start, end) == expected
