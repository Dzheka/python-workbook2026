import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("38.5598\n68.7870\n40.2789\n69.6210\n", "Distance: 204.14 km"),
        ("38.5598\n68.7870\n55.7558\n37.6176\n", "Distance: 2991.43 km"),
        ("55.7558\n37.6176\n40.7128\n-74.0060\n", "Distance: 7510.29 km"),
    ],
)
def test_distance_earth(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
