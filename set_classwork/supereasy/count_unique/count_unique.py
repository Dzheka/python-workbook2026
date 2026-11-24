def count_unique(items):
    return len(set(items))


def all_different(items):
    return count_unique(items) == len(items)