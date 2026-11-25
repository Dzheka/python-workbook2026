def evaluate_postfix(tokens: list[str]) -> float:
    if not tokens:
        return 0.0

    stack = []
    
    for token in tokens:
        if token == "~":
            a = stack.pop()
            stack.append(-a)
        elif token in {"+", "-", "*", "/", "^"}:
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))
            
    return stack[0]
