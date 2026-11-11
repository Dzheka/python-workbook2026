def similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    both = words1 & words2
    union = words1 | words2

    if not union:
        return 1.0

    return round(len(both) / len(union), 2)


def unique_to_first(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    unique_words = words1 - words2

    return sorted(list(unique_words))