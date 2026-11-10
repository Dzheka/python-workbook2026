o = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
t = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def below_100(n):
    if n < 20:
        return o[n]
    t1 = n // 10
    o1 = n % 10
    if (o1 == 0):
        return t[t1]
    return t[t1] + "-" + o[o1]

def below_1000(n):
    h = n // 100
    menshe = n % 100
    ans1 = []
    if h > 0:
        ans1.append(o[h] + " hundred")
    if menshe > 0:
        ans1.append(below_100(menshe))

    return " ".join(ans1)

def number_to_words(n):
    if n == 0:
        return "zero"
    if n < 0:
        return "minus " + number_to_words(-n)
    milioni = n // 1000000
    tisyachi = (n // 1000) % 1000
    menshe = n % 1000 
    ans = []
    if milioni > 0:
        ans.append(below_1000(milioni) + " million")
    if tisyachi > 0:
        ans.append(below_1000(tisyachi) + " thousand")
    if menshe > 0:
        ans.append(below_1000(menshe))

    return " ".join(ans)



l = int(input())

print(number_to_words(l))