"""Read a first name and a last name with two input() calls, then print three lines:

both names in UPPERCASE, separated by one space
the initials, each followed by a dot: initials: B.Q.
the letter counts and their sum: letters: 6 + 7 = 13
The names may be typed in any case — bahrom, Bahrom and BAHROM must all produce the same output."""

name = input()
surname = input()

print(f'{name.upper()} {surname.upper()}')

print(f'initials: {name[0].upper()}.{surname[0].upper()}.')
print(f'letters: {len(name)} + {len(surname)} = {len(name) + len(surname)}')
