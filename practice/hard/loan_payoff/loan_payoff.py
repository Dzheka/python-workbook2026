def monthly_interest(balance, yearly_rate):
    return balance * yearly_rate / 100 / 12


def months_to_repay(loan, yearly_rate, payment):
    if loan <= 0:
        return 0
    if payment <= monthly_interest(loan, yearly_rate):
        return -1

    a = 0
    balance = loan

    while balance > 0:
        balance += monthly_interest(balance, yearly_rate)
        balance -= min(payment, balance)
        a += 1

    return a


def total_paid(loan, yearly_rate, payment):
    if loan <= 0:
        return 0.0
    if payment <= monthly_interest(loan, yearly_rate):
        return -1

    b = 0.0
    balance = loan

    while balance > 0:
        balance += monthly_interest(balance, yearly_rate)
        x = min(payment, balance)
        balance -= x
        b += x

    return round(b, 2)