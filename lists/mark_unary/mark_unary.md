# Mark Unary

Mark unary operators (negative signs) in a tokenized expression.

## Task

- Create a function `mark_unary(tokens)` that takes a list of tokens
- Return a new list with each unary minus (negation) replaced by `'~'`
- A minus is unary when it's the first token, follows `'('`, or follows another operator; otherwise it's binary (subtraction) and stays `'-'`

## Template:

```python
def mark_unary(tokens: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your function
    print(mark_unary(['-', '5', '+', '3']))  # ['~', '5', '+', '3']
    print(mark_unary(['(', '-', '5', ')', '*', '2']))  # ['(', '~', '5', ')', '*', '2']
    print(mark_unary(['3', '-', '5']))  # ['3', '-', '5']
```
