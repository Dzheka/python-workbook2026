""" Write a program that reads an HTTP status code from the user and displays the corresponding category.

HTTP Status Code Categories
Range	Category
100-199	Informational
200-299
300-399	Redirection
400-499	Client Error
500-599	Server Error"""
i = int(input())

if i < 100:
    print('Unknown status code')
elif 100 <= i <= 199:
    print("Informational")
elif 200 <= i <= 299:
    print('Success')
elif 300 <= i <= 399:
    print("Redirection")
elif 400 <= i <= 499:
    print("Client Error")
elif 400 <= i <= 599:
    print("Server Error")
else:
    print('Unknown status code')