import pytest


@pytest.mark.parametrize(
    "name",
    [
        "Farid",
        "Gulnora",
        "Davron",
    ],
)
def test_hello_name(solution, name):
    solution.check_output(input_text=f"{name}\n", expected_output=f"Hello {name}!")
