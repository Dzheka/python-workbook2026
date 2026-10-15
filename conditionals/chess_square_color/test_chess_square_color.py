import pytest


@pytest.mark.parametrize(
    "position, expected_output",
    [
        ("a1", "black"),
        ("a2", "white"),
        ("a7", "black"),
        ("a8", "white"),
        ("b1", "white"),
        ("b2", "black"),
        ("b7", "white"),
        ("c1", "black"),
        ("c2", "white"),
        ("c3", "black"),
        ("c7", "black"),
        ("d1", "white"),
        ("d2", "black"),
        ("d5", "white"),
        ("d7", "white"),
        ("e1", "black"),
        ("e2", "white"),
        ("e4", "white"),
        ("e7", "black"),
        ("f1", "white"),
        ("f2", "black"),
        ("f7", "white"),
        ("g1", "black"),
        ("g2", "white"),
        ("g7", "black"),
        ("h1", "white"),
        ("h2", "black"),
        ("h7", "white"),
        ("h8", "black"),
    ],
)
def test_chess_square_color(solution, position, expected_output):
    solution.check_output(input_text=f"{position}\n", expected_output=expected_output)
