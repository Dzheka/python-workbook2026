# Evaluate Postfix

Evaluate a postfix expression and return the result.

## Task

- Create a function `evaluate_postfix(tokens)` that takes a list of tokens in postfix notation
- Return the numeric result of evaluating the expression

## Template:

```python
def evaluate_postfix(tokens: list[str]) -> float:
    pass


if __name__ == "__main__":
    # Test your function
    print(evaluate_postfix(['3', '5', '2', '*', '+']))  # 13.0 (3 + 5*2)
    print(evaluate_postfix(['3', '5', '+', '2', '*']))  # 16.0 ((3+5)*2)
    print(evaluate_postfix(['15', '7', '1', '1', '+', '-', '/']))  # 3.0
```
