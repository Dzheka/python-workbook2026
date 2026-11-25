def f(n: str):
    if n == "":
        return ""
    else:
        n = int(n)
        if n==1:
            return "one"
        elif n==2:
            return "two"
        elif n==3:
            return "three"
        elif n==4:
            return "four"
        elif n==5:
            return "five"
        elif n==6:
            return "six"
        elif n==7:
            return "seven"
        elif n==8:
            return "eight"
        elif n==9:
            return "nine"
        elif n==10:
            return "ten"
        elif n==11:
            return "eleven"
        elif n==12:
            return "twelve"
        elif n==13:
            return "thirteen"
        elif n==14:
            return "fourteen"
        elif n==15:
            return "fifteen"
        elif n==16:
            return "sixteen"
        elif n==17:
            return "seventeen"
        elif n==18:
            return "eighteen"
        elif n==19:
            return "nineteen"
        elif n==20:
            return "twenty"
        elif n==30:
            return "thirty"
        elif n==40:
            return "forty"
        elif n==50:
            return "fifty"
        elif n==60:
            return "sixty"
        elif n==70:
            return "seventy"
        elif n==80:
            return "eighty"
        elif n==90:
            return "ninety"
def below_100(n: str):
    if n == "":
        return ""
    else:
        n = int(n)
        if n==0:
            return "zero"
        elif abs(n) < 100:
            if n>0:
                if n%10==0 or n<20:
                    return f"{f(abs(n))}"
                else:
                    return f"{f(n-n%10)} {f(n%10)}"
            elif n<0:
                if n%10==0 or abs(n)<20:
                    return f"minus {f(abs(n))}"
                return f"minus {f(abs(n)-abs(n)%10)} {f(abs(n)%10)}"
def read_aloud(n: str):
    if n == "":
        return ""
    else:
        n = int(n)
        if abs(n) <100:
            return below_100(n).upper()
        elif abs(n)<1000:
            if n>0:
                if n%100==0:
                    return f"{f(n//100)} hundred".upper()
                else:
                    return f"{f(n//100)} hundred {below_100(n%100)}".upper()
            else:
                if n%100==0:
                    return f"minus {f(abs(n)//100)} hundred".upper()
                else:
                    return f"minus {f(abs(n)//100)} hundred {below_100(abs(n)%100)}".upper()
print(read_aloud("7"))  
print(read_aloud("15")) 
print(read_aloud("42"))  
print(read_aloud("90"))  
print(read_aloud("100")) 
print(read_aloud("105"))  
print(read_aloud("333"))
print(read_aloud("0"))
print(read_aloud(""))
