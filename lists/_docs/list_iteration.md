# Lists in Python - Iteration and Common Patterns

## Iterating Over Lists

| Method                 | Use Case                        | Example                                  |
|------------------------|---------------------------------|------------------------------------------|
| Basic for loop         | Iterate over values             | `for fruit in fruits: print(fruit)`      |
| With enumerate         | Need index and value            | `for i, fruit in enumerate(fruits):`     |
| With enumerate (start) | Custom starting index           | `for i, x in enumerate(data, start=1):`  |
| With range             | Need index to modify list       | `for i in range(len(fruits)):`           |
| With zip               | Iterate multiple lists together | `for name, score in zip(names, scores):` |
| Reversed               | Iterate in reverse order        | `for num in reversed(numbers):`          |
| With slice             | Iterate over part of list       | `for x in numbers[2:5]:`                 |
| While loop             | Complex iteration logic         | `i = 0` <br> `while i < len(list):`      |

## Common Patterns

| Pattern                 | Built-in Approach                         | Manual Approach                                                      |
|-------------------------|-------------------------------------------|----------------------------------------------------------------------|
| **Sum**                 | `total = sum(numbers)`                    | `total = 0` <br> `for n in numbers: total += n`                      |
| **Average**             | `avg = sum(numbers) / len(numbers)`       | `total = sum(numbers)` <br> `avg = total / len(numbers)`             |
| **Maximum**             | `max_val = max(numbers)`                  | `max_val = numbers[0]` <br> `for n in numbers: ...`                  |
| **Minimum**             | `min_val = min(numbers)`                  | `min_val = numbers[0]` <br> `for n in numbers: ...`                  |
| **Count occurrences**   | `count = numbers.count(value)`            | `count = 0` <br> `for n in numbers: if n == value: count+=1`         |
| **Filter**              | `evens = [n for n in nums if n % 2 == 0]` | `evens = []` <br> `for n in nums: if n % 2 == 0: evens.append(n)`    |
| **Transform**           | `squares = [n ** 2 for n in numbers]`     | `squares = []` <br> `for n in numbers: squares.append(n**2)`         |
| **Search (membership)** | `if value in numbers:`                    | `found = False` <br> `for n in numbers: if n == value: ...`          |
| **Search (index)**      | `index = numbers.index(value)`            | `for i, n in enumerate(nums): if n == value: ...`                    |
| **Build from input**    | `nums = [int(input()) for _ in range(n)]` | `nums = []` <br> `for i in range(n): nums.append(int(input()))`      |
| **Reverse**             | `reversed_list = numbers[::-1]`           | `reversed_list = []` <br> `for i in range(len(nums)-1, -1, -1): ...` |
| **Remove duplicates**   | `unique = list(set(numbers))`             | Manual loop checking if item already in new list                     |
