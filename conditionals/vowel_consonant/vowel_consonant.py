a=str(input())
if a in "aeiouAEIOU":
    print("vowel")
elif a in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
    print("consonant")
else:
    print("sometimes vowel, sometimes consonant")