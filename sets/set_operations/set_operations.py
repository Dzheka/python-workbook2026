def uniques(values: list) -> set:
    result = set()
    for x in values:
        result.add(x)
    return result


def union(set1: set, set2: set) -> set:
    result = set()
    for x in set1:
        result.add(x)
    for x in set2:
        result.add(x)
    return result


def intersection(set1: set, set2: set) -> set:
    result = set()
    for x in set1:
        if x in set2:
            result.add(x)
    return result


def is_subset(subset: set, superset: set) -> bool:
    for x in subset:
        if x not in superset:
            return False
    return True


def symmetric_diff(set1: set, set2: set) -> set:
    if isinstance(set1, set) and isinstance(set2, set):
        result = set()
        for x in set1:
            if x not in set2:
                result.add(x)
        for x in set2:
            if x not in set1:
                result.add(x)
        return result

