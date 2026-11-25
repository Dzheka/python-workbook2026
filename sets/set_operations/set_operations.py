def uniques(values: list):
    a = set()
    for i in values:
        a.add(i)
    return a


def union(set1: set, set2: set):
    a = set()
    for i in set1:
        a.add(i)
    for i in set2:
        a.add(i)
    return a


def intersection(set1: set, set2: set):
    a = set()
    for i in set1:
        if i in set2:
            a.add(i)
    return a


def is_subset(subset: set, superset: set):
    for i in subset:
        if i not in superset:
            return False
    return True


def symmetric_diff(set1: set, set2: set):
    a = set()
    for i in set1:
        if i not in set2:
            a.add(i)
    for i in set2:
        if i not in set1:
            a.add(i)
    return a