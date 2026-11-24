def evaluate_postfix(tokens: list[str]):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '^':
                token = '**'
            stack.append(eval(f'{a} {token} {b}'))
    return float(stack[0])
if __name__ == "__main__":
    # Test your function
    print(evaluate_postfix(['3', '5', '2', '*', '+']))  # 13.0 (3 + 5*2)
    print(evaluate_postfix(['3', '5', '+', '2', '*']))  # 16.0 ((3+5)*2)
    print(evaluate_postfix(['15', '7', '1', '1', '+', '-', '/']))  # 3.0