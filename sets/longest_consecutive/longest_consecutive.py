def longest_consecutive(numbers: list):
    a = set()
    for i in numbers:
        a.add(i)

    b = 0

    for i in a:
        if i - 1 not in a:
            n = i
            c = 1

            while n + 1 in a:
                n += 1
                c += 1

            b = max(b, c)

    return b

