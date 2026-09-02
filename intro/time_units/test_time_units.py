import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("2\n3\n45\n30\n", "186330"),
        ("1\n0\n30\n0\n", "88200"),
        ("0\n2\n15\n45\n", "8145"),
    ],
)
def test_time_units(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
