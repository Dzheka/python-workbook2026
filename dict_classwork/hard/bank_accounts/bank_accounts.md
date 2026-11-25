# Bank Accounts (Hard)

A small bank writes every operation into a log, in order. Each operation is a
tuple:

| Operation                          | Meaning                                         |
|------------------------------------|-------------------------------------------------|
| `("open", name)`                   | open an account with balance `0`                |
| `("deposit", name, amount)`        | put `amount` into the account                   |
| `("withdraw", name, amount)`       | take `amount` out of the account                |
| `("transfer", src, dst, amount)`   | move `amount` from account `src` to `dst`       |

An operation is **rejected** (skipped, nothing changes) if it uses an account
that has not been opened, or if it would make a balance negative. Opening an
account that already exists does nothing and is **not** a rejection.

## Task

- Create a function `balances(log)` that returns a dictionary: account name →
  final balance
- Create a function `rejected(log)` that returns the positions (indexes,
  starting from `0`) of the rejected operations, in order

## Examples

```python
log = [
    ("open", "Ali"),
    ("deposit", "Ali", 100),
    ("open", "Sara"),
    ("transfer", "Ali", "Sara", 30),
    ("withdraw", "Sara", 50),
    ("deposit", "Bek", 10),
    ("withdraw", "Ali", 70),
]
```

| Call             | Returns                      |
|------------------|------------------------------|
| `balances(log)`  | `{"Ali": 0, "Sara": 30}`     |
| `rejected(log)`  | `[4, 5]`                     |

Operation 4 is rejected because Sara has only 30; operation 5 because Bek has
no account.

Hint: write one helper that walks the log once and returns both the
dictionary and the list; `for i, op in enumerate(log)` gives the index.
