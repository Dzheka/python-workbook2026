
def tokenize_expression(expr: str) -> list[str]:
    numbers = []
    current = ""

    for char in expr:
        if char.isdigit():
            current += char
        else:
            if current:
                numbers.append(current)
                current = ""

            if char != " ":
                numbers.append(char)

    if current:
        numbers.append(current)

    return numbers

if __name__ == "__main__":
    # Test your function
    print(tokenize_expression("3+5*2"))  # ['3', '+', '5', '*', '2']
    print(tokenize_expression("(10+20)*3"))  # ['(', '10', '+', '20', ')', '*', '3']
    print(tokenize_expression("15 - 7 + 2"))  # ['15', '-', '7', '+', '2']
