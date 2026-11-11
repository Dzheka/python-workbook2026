def greet_all(names: list[str]) -> list[str]:
    result = []
    for name in names:
        result.append(f"Hello, {name}!")
    return result


def count_long_names(names: list[str]) -> int:
    count = 0
    for name in names:
        if len(name) > 4:
            count += 1
    return count
