import pytest


@pytest.mark.parametrize(
    "name,age",
    [
        ("Farid", "22"),
        ("Gulnora", "35"),
        ("Davron", "18"),
    ],
)
def test_name_age(solution, name, age):
    solution.check_output(
        input_text=f"{name}\n{age}\n",
        expected_output=f"Hello {name}, you are {age} years old.",
    )
