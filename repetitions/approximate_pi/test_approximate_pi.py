def test_approximate_pi(solution):
    result = solution.run(input_text="")

    # Check that output contains 15 lines with approximations
    lines = result.stdout.strip().split("\n")
    numeric_lines = [line for line in lines if any(char.isdigit() for char in line)]

    assert len(numeric_lines) >= 15

    # Check first approximation is 3.0
    assert "3.0" in result.stdout or "3" in result.stdout

    # Check that values are getting closer to pi (around 3.14159)
    import re

    numbers = re.findall(r"\d+\.\d+", result.stdout)
    if len(numbers) >= 15:
        last_approximation = float(numbers[-1])
        # Should be reasonably close to pi
        assert 3.0 < last_approximation < 3.3
