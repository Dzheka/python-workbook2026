# To 3x3 Matrix

Create a function to convert a string of exactly 9 space-separated integers into a 3x3 matrix.

## Template:

```python
def to3x3matrix(string: str) -> list[list[int]]:
    pass


if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("2 3 5 7 11 13 17 19 23")
    for row in matrix:
        print(row)
    # Output:
    # [2, 3, 5]
    # [7, 11, 13]
    # [17, 19, 23]
```
