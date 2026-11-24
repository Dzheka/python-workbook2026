def tokenize_expression(expr: str) -> list[str]:
    result = []
    temp_n = ''

    for i in expr:
        if i.isdigit():
            temp_n += i
        elif i in '+-*/^()':
            if temp_n != '':
                result.append(temp_n)
                temp_n = ''

            result.append(i)

        elif i.isspace():
            if temp_n != '':
                result.append(temp_n)
                temp_n = ''

    if temp_n != '':
        result.append(temp_n)
    return result


if __name__ == "__main__":
    # Test your function
    print(tokenize_expression("3+5*2"))  # ['3', '+', '5', '*', '2']
    print(tokenize_expression("(10+20)*3"))  # ['(', '10', '+', '20', ')', '*', '3']
    print(tokenize_expression("15 - 7 + 2"))  # ['15', '-', '7', '+', '2']

