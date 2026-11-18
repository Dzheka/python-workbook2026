def missing(row):
    return sorted(list(set(range(1, 10)) - set(row)))


def valid_group(row):
    return len(row) == 9 and set(row) == set(range(1, 10))


def has_conflict(row):
    non_zeros = [x for x in row if x != 0]
    return len(non_zeros) != len(set(non_zeros))