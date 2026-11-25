def greet_all(names):
    return [f"Hello, {name}!" for name in names]

def count_long_names(names):
    return len([name for name in names if len(name) > 4])