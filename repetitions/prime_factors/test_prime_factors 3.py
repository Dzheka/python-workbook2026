import pytest


@pytest.mark.parametrize(
    "input_value, expected_factors",
    [
        ("72", ["2", "2", "2", "3", "3"]),
        ("17", ["17"]),
        ("12", ["2", "2", "3"]),
        ("100", ["2", "2", "5", "5"]),
        ("2", ["2"]),
    ],
)
def test_prime_factors(solution, input_value, expected_factors):
    result = solution.run(input_text=f"{input_value}\n")

    # Check that all expected factors appear in output
    for factor in expected_factors:
        assert factor in result.stdout


def test_prime_factors_error(solution):
    result = solution.run(input_text="1\n")

    assert "error" in result.stdout.lower()
