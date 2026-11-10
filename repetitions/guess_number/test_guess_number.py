def test_guess_number(solution):
    # The target is random, so guess every value in range: one of them lands,
    # and the game exits on its own instead of dying on end-of-input.
    every_guess = "".join(f"{n}\n" for n in range(1, 101))

    result = solution.run(input_text=every_guess)

    assert "Correct" in result.stdout
