import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("6.5\n7\n6\n", "subtotal   45.50\ndiscount    2.73\ntotal      42.77"),
        ("10.00\n3\n15\n", "subtotal   30.00\ndiscount    4.50\ntotal      25.50"),
        # No discount at all: the line must still be printed, as 0.00.
        ("4.25\n8\n0\n", "subtotal   34.00\ndiscount    0.00\ntotal      34.00"),
        ("12.99\n5\n20\n", "subtotal   64.95\ndiscount   12.99\ntotal      51.96"),
        # A price whose cents do not survive an int() -- 23.31, not 21.00.
        ("7.77\n3\n9\n", "subtotal   23.31\ndiscount    2.10\ntotal      21.21"),
        # Everything off, and values wide enough to fill the 6-character column.
        ("99.99\n9\n100\n", "subtotal  899.91\ndiscount  899.91\ntotal       0.00"),
    ],
)
def test_bill(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
