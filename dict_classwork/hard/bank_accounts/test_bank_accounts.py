import threading

import pytest

bank_accounts = pytest.importorskip(
    "bank_accounts", reason="bank_accounts.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(bank_accounts, name, None)
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


LOG = [
    ("open", "Ali"),
    ("deposit", "Ali", 100),
    ("open", "Sara"),
    ("transfer", "Ali", "Sara", 30),
    ("withdraw", "Sara", 50),
    ("deposit", "Bek", 10),
    ("withdraw", "Ali", 70),
]

BUSY = [
    ("open", "A"),
    ("open", "B"),
    ("deposit", "A", 50),
    ("open", "A"),
    ("transfer", "A", "C", 10),
    ("transfer", "B", "A", 1),
    ("transfer", "A", "B", 50),
    ("withdraw", "A", 1),
    ("open", "C"),
    ("transfer", "B", "C", 20),
    ("deposit", "C", 5),
]


@pytest.mark.parametrize(
    "log, expected",
    [
        (LOG, {"Ali": 0, "Sara": 30}),
        (BUSY, {"A": 0, "B": 30, "C": 25}),
        ([], {}),
        ([("deposit", "Ali", 5)], {}),
        ([("open", "Ali"), ("open", "Ali")], {"Ali": 0}),
    ],
)
def test_balances(log, expected):
    assert function("balances")(log) == expected


@pytest.mark.parametrize(
    "log, expected",
    [
        (LOG, [4, 5]),
        (BUSY, [4, 5, 7]),
        ([], []),
        ([("deposit", "Ali", 5)], [0]),
        ([("open", "Ali"), ("open", "Ali")], []),
        ([("open", "Ali"), ("withdraw", "Ali", 0)], []),
    ],
)
def test_rejected(log, expected):
    assert function("rejected")(log) == expected


def test_log_is_not_changed():
    log = list(LOG)
    function("balances")(log)
    function("rejected")(log)
    assert log == LOG
