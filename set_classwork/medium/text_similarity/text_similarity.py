def similarity(text1, text2):
    a = set(text1.lower().split())
    b = set(text2.lower().split())
    all_words = a | b

    if not all_words:
        return 1.0

    shared_words = a & b
    return round(len(shared_words) / len(all_words), 2)


def unique_to_first(text1, text2):
    a = set(text1.lower().split())
    b = set(text2.lower().split())
    return sorted(a - b)