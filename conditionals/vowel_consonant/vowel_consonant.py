letter = input().lower()

if letter in "aeiou":
    print("vowel")
elif letter == "y":
    print("sometimes vowel, sometimes consonant")
else:
    print("consonant")