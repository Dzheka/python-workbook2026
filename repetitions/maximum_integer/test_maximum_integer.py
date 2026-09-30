def test_maximum_integer(solution):
    result = solution.run(input_text="")

    # Check for key phrases in output
    assert "maximum" in result.stdout.lower()
    assert "update" in result.stdout.lower()

    # Check that there are roughly 100 numbers displayed
    # Count lines with numbers
    lines = result.stdout.strip().split("\n")
    numeric_lines = [line for line in lines if any(char.isdigit() for char in line)]

    # Should have around 100 numbers plus summary lines
    assert len(numeric_lines) >= 90  # Allow some flexibility
