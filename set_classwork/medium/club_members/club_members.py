def in_both(chess, football):
    return sorted(set(chess) & set(football))


def in_exactly_one(chess, football):
    return sorted(set(chess) ^ set(football))


def in_neither(students, chess, football):
    a = set(chess) | set(football)
    return sorted(set(students) - a)