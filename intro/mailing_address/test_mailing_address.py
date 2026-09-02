def test_mailing_address(solution):
    # The address is the student's own, so only its shape can be graded.
    # solution.run() already fails the test if the script asks for input,
    # since it is given none and input() would raise EOFError.
    result = solution.run()

    lines = [line for line in result.stdout.strip().split("\n") if line.strip()]

    # At minimum a name, a street and a city -- one line is not an address.
    assert len(lines) >= 3
