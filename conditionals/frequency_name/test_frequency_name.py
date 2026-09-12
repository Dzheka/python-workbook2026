import pytest


@pytest.mark.parametrize(
    "frequency, expected_output",
    [
        (100000000, "Radio Waves"),  # 1 × 10⁸
        (1000000000, "Radio Waves"),  # 1 × 10⁹
        (2000000000, "Radio Waves"),  # 2 × 10⁹ (< 3 × 10⁹)
        (3000000000, "Microwaves"),  # 3 × 10⁹ (boundary)
        (10000000000, "Microwaves"),  # 1 × 10¹⁰
        (2000000000000, "Microwaves"),  # 2 × 10¹² (< 3 × 10¹²)
        (3000000000000, "Infrared Light"),  # 3 × 10¹² (boundary)
        (400000000000000, "Infrared Light"),  # 4 × 10¹⁴ (< 4.3 × 10¹⁴)
        (430000000000000, "Visible Light"),  # 4.3 × 10¹⁴ (boundary)
        (500000000000000, "Visible Light"),  # 5 × 10¹⁴
        (600000000000000, "Visible Light"),  # 6 × 10¹⁴
        (750000000000000, "Ultraviolet Light"),  # 7.5 × 10¹⁴ (boundary)
        (300000000000000000, "X-Rays"),  # 3 × 10¹⁷ (boundary)
        (1000000000000000000, "X-Rays"),  # 1 × 10¹⁸
        (30000000000000000000, "Gamma Rays"),  # 3 × 10¹⁹ (boundary)
        (100000000000000000000, "Gamma Rays"),  # 1 × 10²⁰
    ],
)
def test_frequency_name(solution, frequency, expected_output):
    solution.check_output(input_text=f"{frequency}\n", expected_output=expected_output)
