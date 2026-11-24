letter = input().lower()

if letter == "y":
    print("sometimes vowel, sometimes consonant")
elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("vowel")
else:
    print("consonant")