import pytest


@pytest.mark.parametrize(
    "age, expected_output",
    [
        (0, "cannot vote"),
        (17, "cannot vote"),
        (18, "can vote"),
        (25, "can vote"),
        (65, "can vote"),
    ],
)
def test_can_vote(solution, age, expected_output):
    solution.check_output(input_text=f"{age}\n", expected_output=expected_output)
