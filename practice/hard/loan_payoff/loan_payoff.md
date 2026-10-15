# Paying Off a Loan (Hard)

You borrow money at a yearly interest rate and pay a fixed amount every
month. Each month:

1. interest is added: `balance · yearly_rate / 100 / 12`
2. then your payment is taken off

When the balance is smaller than the payment, the last payment is just the
remaining balance. If the payment does not even cover the first month's
interest, the loan is never repaid.

## Task

- Create a function `monthly_interest(balance, yearly_rate)` that returns
  one month's interest
- Create a function `months_to_repay(loan, yearly_rate, payment)` that
  returns how many monthly payments it takes, or `-1` if the loan is never
  repaid
- Create a function `total_paid(loan, yearly_rate, payment)` that returns
  how much money you pay in total, rounded to 2 decimals, or `-1` if the loan
  is never repaid

## Examples

| Call                                  | Returns    |
|---------------------------------------|------------|
| `monthly_interest(1000, 12)`          | `10.0`     |
| `monthly_interest(1500, 18)`          | `22.5`     |
| `months_to_repay(1000, 12, 100)`      | `11`       |
| `months_to_repay(5000, 0, 500)`       | `10`       |
| `months_to_repay(10000, 24, 200)`     | `-1`       |
| `months_to_repay(10000, 24, 201)`     | `268`      |
| `total_paid(1000, 12, 100)`           | `1058.98`  |
| `total_paid(300, 5, 1000)`            | `301.25`   |

In the third example the interest is exactly 200 a month, so the balance
never goes down. One more per month, and it takes over 22 years.
