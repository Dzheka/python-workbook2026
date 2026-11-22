import threading

import pytest

sales_report = pytest.importorskip(
    "sales_report", reason="sales_report.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(sales_report, name, None)
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


SALES = [
    ("Sughd", "tea", 120),
    ("Khatlon", "rice", 300),
    ("Sughd", "rice", 80),
    ("Sughd", "tea", 50),
    ("Khatlon", "tea", 40),
    ("GBAO", "honey", 90),
]

TIES = [
    ("North", "plum", 10),
    ("North", "apple", 4),
    ("North", "apple", 6),
    ("South", "kiwi", 5),
]


@pytest.mark.parametrize(
    "sales, expected",
    [
        (SALES, {"Sughd": 250, "Khatlon": 340, "GBAO": 90}),
        (TIES, {"North": 20, "South": 5}),
        ([], {}),
    ],
)
def test_by_region(sales, expected):
    assert function("by_region")(sales) == expected


@pytest.mark.parametrize(
    "sales, expected",
    [
        (
            SALES,
            {
                "Sughd": {"tea": 170, "rice": 80},
                "Khatlon": {"rice": 300, "tea": 40},
                "GBAO": {"honey": 90},
            },
        ),
        (TIES, {"North": {"plum": 10, "apple": 10}, "South": {"kiwi": 5}}),
        ([], {}),
    ],
)
def test_report(sales, expected):
    assert function("report")(sales) == expected


@pytest.mark.parametrize(
    "sales, expected",
    [
        (SALES, {"Sughd": "tea", "Khatlon": "rice", "GBAO": "honey"}),
        (TIES, {"North": "apple", "South": "kiwi"}),
        ([], {}),
    ],
)
def test_best_sellers(sales, expected):
    assert function("best_sellers")(sales) == expected


def test_sales_are_not_changed():
    sales = list(SALES)
    function("report")(sales)
    function("best_sellers")(sales)
    assert sales == SALES
