def reverse_list(string: str) -> list[int]:
    a = [int(word) for word in string.split()]
    return a[::-1]