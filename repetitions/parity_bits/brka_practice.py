def digit_sum(n):
    ans = 0
    while(n > 0):
        ans += n % 10
        n = n // 10
    return ans
def is_lucky(t):
    x = digit_sum(t % 1000)
    y = digit_sum(t // 1000)
    return x == y

a = int(input())
b = int(input())
vivod = 0
for i in range (a, b + 1):
    if is_lucky(i):
        vivod += 1
print(vivod)

