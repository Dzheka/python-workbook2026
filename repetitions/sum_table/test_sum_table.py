def test_sum_table(solution):
    result = solution.run(input_text="")

    assert "18" in result.stdout  # 9 + 9
    assert "16" in result.stdout  # 8 + 8
    assert "14" in result.stdout  # 7 + 7

    lines = result.stdout.strip().split("\n")
    assert len(lines) == 10
