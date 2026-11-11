def to3x3matrix(string: str) -> list[list[int]]:
    numbers = []
    for i in  string.split():
        numbers.append(int(i))
    numbers = numbers[::-1] # to improve performance although it doesnt matter in this case
    matrix = []
    for i in range(0, 3):
        current_row = []
        for j in range(0, 3):
            current_row.append(numbers.pop())
        matrix.append(current_row)
    return matrix



if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("2 3 5 7 11 13 17 19 23")
    for row in matrix:
        print(row)
    # Output:
    # [2, 3, 5]
    # [7, 11, 13]
    # [17, 19, 23]