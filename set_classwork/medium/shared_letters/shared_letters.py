def common_letters(words):
    if not words:
        return []

    # Start with the lowercase letters of the first word
    common = set(c.lower() for c in words[0] if c.isalpha())

    # Keep only what each subsequent word also has
    for word in words[1:]:
        word_letters = set(c.lower() for c in word if c.isalpha())
        common &= word_letters

    return sorted(list(common))


def any_letters(words):
    if not words:
        return []

    any_set = set()

    # Accumulate letters from all words
    for word in words:
        word_letters = set(c.lower() for c in word if c.isalpha())
        any_set |= word_letters

    return sorted(list(any_set))