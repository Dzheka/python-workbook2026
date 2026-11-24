a = set(range(1, 10))


def missing(row):
    return sorted(a - set(row))


def valid_group(row):
    return len(row) == 9 and set(row) == a


def has_conflict(row):
    a = [i for i in row if i != 0]
    return len(a) != len(set(a))