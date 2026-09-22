def test_fizz_buzz(solution):
    result = solution.run(input_text="")

    lines = result.stdout.strip().split("\n")

    # Should have 100 lines
    assert len(lines) == 100

    # Check specific values
    assert lines[0] == "1"
    assert lines[1] == "2"
    assert lines[2] == "fizz"
    assert lines[3] == "4"
    assert lines[4] == "buzz"
    assert lines[5] == "fizz"
    assert lines[14] == "fizzbuzz"
    assert lines[29] == "fizzbuzz"
    assert lines[99] == "buzz"
