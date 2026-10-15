import re


def test_approximate_pi(solution):
    result = solution.run(input_text="")

    lines = result.stdout.strip().split("\n")
    approximation_lines = [
        line for line in lines if any(char.isdigit() for char in line)
    ]

    assert len(approximation_lines) >= 15

    # Check first approximation is 3.0
    assert "3.0" in result.stdout or "3" in result.stdout

    # Check that values are getting closer to pi (around 3.14159)
    numbers = re.findall(r"\d+\.\d+", result.stdout)
    if len(numbers) >= 15:
        last_approximation = float(numbers[-1])
        assert 3.0 < last_approximation < 3.3
