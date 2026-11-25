def list_to_string(words: list[str]) -> str:
    return " ".join(words)


if __name__ == "__main__":
    # Test your function
    print(list_to_string(["Hello", "world"]))  # "Hello world"
    print(list_to_string(["Python", "is", "fun"]))  # "Python is fun"
    print(list_to_string([]))  # ""
