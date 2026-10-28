letter = input().lower()

if letter == "y":
    print("sometimes vowel, sometimes consonant")
elif letter in "aeiou":
    print("vowel")
else:
    print("consonant")
