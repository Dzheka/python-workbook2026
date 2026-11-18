from typing import Callable


def filter_list(l: list, condition: Callable) -> list:
    numbers = []
    for i in l:
        if condition(i):
            numbers.append(i)
    return numbers
    


if __name__ == "__main__":
    # Test your function
    def is_even(x):
        return x % 2 == 0


    print(filter_list([11, 4, 7, 22, 9], is_even))  # [4, 22]


    def is_positive(x):
        return x > 0


    print(filter_list([-2, -1, 0, 1, 2], is_positive))  # [1, 2]
