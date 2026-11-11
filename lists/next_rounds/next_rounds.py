def next_rounds(n: int) -> list[int]:
    r = []
    for i in range(n + 1, n + 4):
        r.append(i)
    return r


if __name__ == "__main__":
    # Test your function
    print(next_rounds(27))  # [28, 29, 30]
    print(next_rounds(0))  # [1, 2, 3]