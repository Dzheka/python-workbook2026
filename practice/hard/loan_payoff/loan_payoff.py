def monthly_interest(b, y):
    return b * y / 100 / 12
def months_to_repay(l, y, p):
    if p <= monthly_interest(l, y):
        return -1
    b = l
    m = 0
    while b > 0:
        i = monthly_interest(b, y)
        b += i
        if b <= p:
            m += 1
            break
        b -= p
        m += 1
        if m > 10000:
            return -1
        return m
def total_paid(l, y, p):
    if p <= monthly_interest(l, y):
        return -1
    b = l
    t = 0.0
    while b > 0:
        i = monthly_interest(b, y)
        b += i
        if b <= p:
            t += b
            break
        b -= p
        t += p
        if t > 1e10:
            return -1
    return round(t, 2)