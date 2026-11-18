grades = ['4.0', '4.0', '3.7', '3.3', '3.0', '2.7', '2.3', '2.0', '1.7', '1.3', '1.0', '0.0']
letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+',	'D', 'F']
letter_grade = input()

if letter_grade in letter_grades:
    i = letter_grades.index(letter_grade)
    print(grades[i])
else:
    print('Invalid grade')