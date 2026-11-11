
from lists.precedence.precedence import precedence


def infix_to_postfix(tokens: list[str]) -> list[str]:
    output = []
    stack = []

    for token in tokens:

        if token.isdigit():
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('

        else:
            while (stack and
                   stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


if __name__ == "__main__":
    print(infix_to_postfix(['3', '+', '5', '*', '2']))
    # ['3', '5', '2', '*', '+']

    print(infix_to_postfix(['(', '3', '+', '5', ')', '*', '2']))
    # ['3', '5', '+', '2', '*']
