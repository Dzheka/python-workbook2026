a = input().lower()
if a in ("a", "e", "i", "o", "u"):
    print("vowel")
elif a == "y":
    print("sometimes vowel, sometimes consonant")
else:
    print("consonant")