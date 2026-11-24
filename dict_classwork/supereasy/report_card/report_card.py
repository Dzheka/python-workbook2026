def average(grades):
    if not grades:
        return 0

    return round(sum(grades.values()) / len(grades), 1)


def best_student(grades):
    a = None

    for i in sorted(grades):
        if a is None or grades[i] > grades[a]:
            a = i

    return a


def passed(grades, limit):
    a = []

    for i, b in grades.items():
        if b >= limit:
            a.append(i)

    return sorted(a)