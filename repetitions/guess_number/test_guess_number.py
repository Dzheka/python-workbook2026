def test_guess_number(solution):
    # The secret number is random, so the test cannot follow the hints. Guessing
    # 1, 2, 3 ... 100 in order is guaranteed to reach it whatever it is, which
    # makes the run deterministic: every wrong guess prints a hint and the last
    # one wins.
    guesses = "".join(f"{n}\n" for n in range(1, 101))
    result = solution.run(input_text=guesses)

    assert "Correct" in result.stdout
    assert "Too low" in result.stdout or "Too high" in result.stdout
