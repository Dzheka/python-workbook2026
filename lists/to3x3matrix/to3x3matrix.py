def to3x3matrix(string: str) -> list[list[int]]:
    a = [int(word) for word in string.split()]
    return [a[0:3], a[3:6], a[6:9]]