def in_both(chess, football):
    return sorted(set(chess) & set(football))

def in_exactly_one(chess, football):
    return sorted(set(chess) ^ set(football))

def in_neither(students, chess, football):
    students = set(students)
    students -= set(chess)
    students -= set(football)
    return sorted(students)

