code = int(input())

if 100 <= code <= 199:
    print("Informational")
elif 200 <= code <= 299:
    print("Success")
elif 300 <= code <= 399:
    print("Redirection")
elif 400 <= code <= 499:
    print("Client Error")
elif 500 <= code <= 599:
    print("Server Error")
else:
    print("Unknown status code")