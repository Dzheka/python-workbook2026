def test_maximum_integer(solution):
    result = solution.run(input_text="")

    assert "maximum" in result.stdout.lower()
    assert "update" in result.stdout.lower()

    lines = result.stdout.strip().split("\n")
    numeric_lines = [line for line in lines if any(char.isdigit() for char in line)]

    # ~100 numbers are displayed; 90 leaves slack for formatting differences
    assert len(numeric_lines) >= 90
