def luhn_sum(number):
    sum = 0
    is_second = False
    for i in number[::-1]:
        n = int(i)

        if is_second:
            is_second = False
        else:
            is_second = True
            sum += n
            continue

        if n * 2 > 9:
            sum += n * 2 - 9
        else:
            sum += n * 2
    return sum

def is_valid_card(number):
    if len(number) <= 2:
        return False
    if not number.isdigit():
        return False
    if luhn_sum(number) % 10 == 0:
        return True
    return False

def check_digit(number):
    s = luhn_sum(number + "0")
    return (10 - (s % 10)) % 10

def mask(number):
    result = ''
    c = 0
    for i in number[::-1]:
        if c < 4:
            result += i
        else:
            result += '*'
        c += 1
    return result[::-1]

print(luhn_sum("79927398713"))
print(luhn_sum("79927398710"))
print(is_valid_card("79927398713"))
print(is_valid_card("4539148803436467"))
print(is_valid_card("4539148803436468"))
print(is_valid_card("12a4"))
print(is_valid_card("0"))
print(check_digit("7992739871"))
print(check_digit("453914880343646"))
print(mask("4539148803436467"))
print(mask("1234"))