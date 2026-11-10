def test_coin_flip(solution):
    result = solution.run(input_text="")

    assert "flip" in result.stdout.lower()
    assert "average" in result.stdout.lower()
    assert "H" in result.stdout or "T" in result.stdout

    lines = result.stdout.strip().split("\n")
    flip_lines = [line for line in lines if "H" in line or "T" in line]
    assert len(flip_lines) >= 10
