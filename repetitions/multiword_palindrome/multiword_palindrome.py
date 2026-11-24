raw_input = input()

string = ''.join(char.lower() for char in raw_input if char.isalnum())
if string == string[::-1]:
    print('palindrome')
else:
    print('not a palindrome')