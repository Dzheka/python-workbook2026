import pytest

run_length = pytest.importorskip("run_length", reason="run_length.py not implemented")


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(run_length, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("z", "z"),
        ("abc", "abc"),
        ("aaabccdd", "3ab2c2d"),
        # The same letter in two separate runs.
        ("aabbaa", "2a2b2a"),
        ("aaaaaaaaaaaa", "12a"),
        ("WWWWWWWWWWWWBWWWWWWWWWWWWBBB", "12WB12W3B"),
    ],
)
def test_encode(text, expected):
    assert function("encode")(text) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("", ""),
        ("abc", "abc"),
        ("3ab2c2d", "aaabccdd"),
        ("2a2b2a", "aabbaa"),
        ("12a", "aaaaaaaaaaaa"),
        ("10x1y", "xxxxxxxxxxy"),
    ],
)
def test_decode(code, expected):
    assert function("decode")(code) == expected


@pytest.mark.parametrize(
    "text",
    ["hello", "aaaaaaaaaaaaaaab", "xyyzzzyyx", "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"],
)
def test_decode_reverses_encode(text):
    encode, decode = function("encode"), function("decode")
    assert decode(encode(text)) == text


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aaabccdd", True),
        ("aaab", True),
        # "2a2b" is as long as the original, not shorter.
        ("aabb", False),
        ("abc", False),
        ("", False),
    ],
)
def test_is_worth_it(text, expected):
    assert function("is_worth_it")(text) is expected
