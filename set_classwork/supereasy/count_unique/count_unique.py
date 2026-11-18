def count_unique(items: list[int]) -> int:
    new_list = []
    for i in items:
        if i not in new_list:
            new_list.append(i)
    return len(new_list)


def all_different(items):
    if len(items) == count_unique(items):
        return True
    return False