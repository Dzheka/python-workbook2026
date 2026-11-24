def rotate_left(items: list, k: int) -> list:
    if not items:
        return []

    k = k % len(items)
    return items[k:] + items[:k]

def rotate_right(items: list, k: int) -> list:
    if not items:
        return []

    k = k % len(items)
    return items[-k:] + items[:-k] if k else items[:]


def is_rotation(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False

    for k in range(len(a)):
        if rotate_left(a, k) == b:
            return True

    return a == b if not a else False
