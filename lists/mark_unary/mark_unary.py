def mark_unary(tokens: list[str]) -> list[str]:
    stack = []
    for i_token in range(0, len(tokens) - 1):
        token = tokens[i_token]
        if token.isdigit():
            stack.append(int(token))
        if token == '-':
            if i_token == 0 or tokens[i_token - 1] in '+-*/^(':
                tokens[i_token] = '~'
    return tokens


if __name__ == "__main__":
    # Test your function
    print(mark_unary(['-', '5', '+', '3']))  # ['~', '5', '+', '3']
    print(mark_unary(['(', '-', '5', ')', '*', '2']))  # ['(', '~', '5', ')', '*', '2']
    print(mark_unary(['3', '-', '5']))  # ['3', '-', '5']
