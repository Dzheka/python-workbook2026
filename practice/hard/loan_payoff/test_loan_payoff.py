import threading

import pytest

loan_payoff = pytest.importorskip(
    "loan_payoff", reason="loan_payoff.py not implemented"
)

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(loan_payoff, name, None)
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
    "balance, yearly_rate, expected",
    [
        (1000, 12, 10.0),
        (2400, 6, 12.0),
        (5000, 0, 0.0),
        (1500, 18, 22.5),
    ],
)
def test_monthly_interest(balance, yearly_rate, expected):
    assert function("monthly_interest")(balance, yearly_rate) == pytest.approx(
        expected, abs=0.01
    )


@pytest.mark.parametrize(
    "loan, yearly_rate, payment, expected",
    [
        (1000, 12, 100, 11),
        (5000, 0, 500, 10),
        (5000, 0, 501, 10),
        (10000, 24, 200, -1),
        (10000, 24, 201, 268),
        (12000, 10, 300, 49),
        (300, 5, 1000, 1),
    ],
)
def test_months_to_repay(loan, yearly_rate, payment, expected):
    assert function("months_to_repay")(loan, yearly_rate, payment) == expected


@pytest.mark.parametrize(
    "loan, yearly_rate, payment, expected",
    [
        (1000, 12, 100, 1058.98),
        (5000, 0, 500, 5000.0),
        (10000, 24, 200, -1),
        (12000, 10, 300, 14657.63),
        (300, 5, 1000, 301.25),
    ],
)
def test_total_paid(loan, yearly_rate, payment, expected):
    assert function("total_paid")(loan, yearly_rate, payment) == pytest.approx(
        expected, abs=0.01
    )
