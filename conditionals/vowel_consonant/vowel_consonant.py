"""Logic
If letter is 'y': display "sometimes vowel, sometimes consonant"
If letter is 'a', 'e', 'i', 'o', 'u' (case-insensitive): display "vowel"
If the letter is any other alphabetic character: display "consonant"
Note
Handle both uppercase and lowercase letters
The letter 'y' is a special case in English - it can function as either a vowel or consonant depending on context
Vowels are: a, e, i, o, u
All other letters of the alphabet are consonants"""
letter = input()
vowels = 'aeiouAEIOU'

if letter in vowels:
    print("vowel")
elif letter == 'y' or letter == 'Y':
    print("sometimes vowel, sometimes consonant")
else:
    print("consonant")