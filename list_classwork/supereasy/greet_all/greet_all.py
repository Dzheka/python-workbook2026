def greet_all(names):
    result = []
    for name in names:
        result.append(f"Hello, {name}!")
    return result


def count_long_names(names):
    count = 0
    for name in names:
        if len(name) > 4:
            count += 1
    return count