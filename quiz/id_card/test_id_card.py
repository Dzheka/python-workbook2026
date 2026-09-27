import pytest

# Names are read, not hardcoded: every case uses a different pair, so a program
# that just prints its author's own ID card cannot pass.
CASES = [
    ("bahrom\nqosimov\n", "BAHROM QOSIMOV\ninitials: B.Q.\nletters: 6 + 7 = 13"),
    ("malika\nrahimova\n", "MALIKA RAHIMOVA\ninitials: M.R.\nletters: 6 + 8 = 14"),
    ("ali\nnazarov\n", "ALI NAZAROV\ninitials: A.N.\nletters: 3 + 7 = 10"),
    (
        "shohruh\nabdullozoda\n",
        "SHOHRUH ABDULLOZODA\ninitials: S.A.\nletters: 7 + 11 = 18",
    ),
]


@pytest.mark.parametrize("input_params, expected_output", CASES)
def test_id_card(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("Bahrom\nQosimov\n", "BAHROM QOSIMOV\ninitials: B.Q.\nletters: 6 + 7 = 13"),
        ("MALIKA\nRahimova\n", "MALIKA RAHIMOVA\ninitials: M.R.\nletters: 6 + 8 = 14"),
    ],
)
def test_id_card_ignores_input_case(solution, input_params, expected_output):
    # The same names typed capitalised or shouted must give the same card, so
    # the output has to be built with .upper(), not copied from the input.
    solution.check_output(input_text=input_params, expected_output=expected_output)
