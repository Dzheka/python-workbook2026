"""Write a program that determines the color of
 a chess square based on its position."""

square = input()
letter = square[0]
number = int(square[1])

letters = ' abcdefgh'
letter_num = letters.index(letter)

if (number +  letter_num) % 2 == 0:
    print('black')
else:
    print('white')