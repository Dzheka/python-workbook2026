import pytest

try:
    from group_anagrams import group_anagrams
except ImportError:
    group_anagrams = None

pytestmark = pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)


def normalized(groups: list[list[str]]) -> list[list[str]]:
    """Sort within and across groups, since the exercise fixes neither order."""
    return sorted(sorted(group) for group in groups)


def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert normalized(result) == expected


def test_no_anagrams():
    result = group_anagrams(["abc", "def"])
    assert len(result) == 2
    assert ["abc"] in result
    assert ["def"] in result


def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert len(result) == 1
    assert sorted(result[0]) == ["abc", "bca", "cab"]


def test_empty_list():
    assert group_anagrams([]) == []


def test_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]


def test_empty_strings():
    result = group_anagrams(["", ""])
    assert result == [["", ""]]


def test_single_char_words():
    result = group_anagrams(["a", "b", "a"])
    expected = [["a", "a"], ["b"]]
    assert normalized(result) == expected
