def test_multiplication_table(solution):
    result = solution.run(input_text="")

    assert "81" in result.stdout  # 9 × 9
    assert "64" in result.stdout  # 8 × 8
    assert "49" in result.stdout  # 7 × 7

    lines = result.stdout.strip().split("\n")
    assert len(lines) == 9
