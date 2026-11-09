import ast
from pathlib import Path

import pytest

try:
    import set_operations
    from set_operations import intersection, is_subset, symmetric_diff, union, uniques
except ImportError:
    set_operations = None
    intersection = is_subset = symmetric_diff = union = uniques = None

pytestmark = pytest.mark.skipif(
    set_operations is None, reason="set_operations not implemented"
)

BANNED_METHODS = {
    "union",
    "intersection",
    "difference",
    "symmetric_difference",
    "issubset",
    "issuperset",
    "isdisjoint",
    "update",
    "intersection_update",
    "difference_update",
    "symmetric_difference_update",
}
BANNED_BINOPS = (ast.BitOr, ast.BitAnd, ast.BitXor, ast.Sub)
BANNED_COMPARES = (ast.Lt, ast.LtE, ast.Gt, ast.GtE)


def nodes_inside_functions(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            yield from ast.walk(node)


def test_no_set_shortcuts():
    source = Path(set_operations.__file__).read_text()
    for node in nodes_inside_functions(ast.parse(source)):
        assert not isinstance(node, (ast.Set, ast.SetComp)), (
            "set literals and set comprehensions are not allowed"
        )
        if isinstance(node, ast.Name):
            assert node.id != "frozenset", "frozenset is not allowed"
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "set":
                assert not node.args and not node.keywords, (
                    "only empty set() is allowed"
                )
        if isinstance(node, ast.Attribute):
            assert node.attr not in BANNED_METHODS, f".{node.attr}() is not allowed"
        if isinstance(node, (ast.BinOp, ast.AugAssign)):
            assert not isinstance(node.op, BANNED_BINOPS), (
                "the |, &, -, ^ operators are not allowed"
            )
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, BANNED_COMPARES) for op in node.ops), (
                "the <, <=, >, >= comparisons are not allowed"
            )


def check(result, expected):
    assert isinstance(result, set)
    assert result == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 3, 3, 5, 5, 5], {2, 3, 5}),
        (["a", "b", "a", "c", "b"], {"a", "b", "c"}),
        ([], set()),
        ([7, 7, 7, 7], {7}),
        ([2, 3, 5, 7], {2, 3, 5, 7}),
        ([5], {5}),
        ([2, "a", 2, "a", 3], {2, "a", 3}),
    ],
)
def test_uniques(values, expected):
    check(uniques(values), expected)


@pytest.mark.parametrize(
    "set1, set2, expected",
    [
        ({2, 3, 5}, {5, 7, 11}, {2, 3, 5, 7, 11}),
        ({"a", "b"}, {"b", "c", "d"}, {"a", "b", "c", "d"}),
        (set(), {2, 3}, {2, 3}),
        ({2, 3}, set(), {2, 3}),
        (set(), set(), set()),
        ({2, 3}, {5, 7}, {2, 3, 5, 7}),
        ({2, 3, 5}, {2, 3, 5}, {2, 3, 5}),
    ],
)
def test_union(set1, set2, expected):
    check(union(set1, set2), expected)


@pytest.mark.parametrize(
    "set1, set2, expected",
    [
        ({2, 3, 5, 7}, {5, 7, 11, 13}, {5, 7}),
        ({"a", "b", "c"}, {"b", "c", "d"}, {"b", "c"}),
        ({2, 3}, {5, 7}, set()),
        (set(), {2, 3, 5}, set()),
        ({2, 3, 5}, set(), set()),
        (set(), set(), set()),
        ({2, 3, 5}, {2, 3, 5}, {2, 3, 5}),
        ({2, 3}, {2, 3, 5, 7}, {2, 3}),
    ],
)
def test_intersection(set1, set2, expected):
    check(intersection(set1, set2), expected)


@pytest.mark.parametrize(
    "subset, superset, expected",
    [
        ({2, 3}, {2, 3, 5, 7}, True),
        ({2, 11}, {2, 3, 5, 7}, False),
        (set(), {2, 3, 5}, True),
        ({2, 3, 5}, {2, 3, 5}, True),
        ({"a", "b"}, {"a", "b", "c"}, True),
        ({2}, set(), False),
        (set(), set(), True),
        ({2, 3, 5, 7}, {2, 3}, False),
        ({3}, {2, 3, 5}, True),
        ({11}, {2, 3, 5}, False),
    ],
)
def test_is_subset(subset, superset, expected):
    assert is_subset(subset, superset) is expected


@pytest.mark.parametrize(
    "set1, set2, expected",
    [
        ({2, 3, 5}, {3, 5, 7}, {2, 7}),
        ({"a", "b", "c"}, {"b", "c", "d"}, {"a", "d"}),
        ({2, 3}, {2, 3}, set()),
        ({2, 3}, {5, 7}, {2, 3, 5, 7}),
        (set(), {2, 3}, {2, 3}),
        ({2, 3}, set(), {2, 3}),
        (set(), set(), set()),
        ({2, 3, 5}, {5, 7, 11}, {2, 3, 7, 11}),
    ],
)
def test_symmetric_diff(set1, set2, expected):
    check(symmetric_diff(set1, set2), expected)
