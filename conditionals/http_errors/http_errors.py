status = int(input())

if 100 <= status <= 199:
    print("Informational")
elif 200 <= status <= 299:
    print("Success")
elif 300 <= status <= 399:
    print("Redirection")
elif 400 <= status <= 499:
    print("Client Error")
elif 500 <= status <= 599:
    print("Server Error")
else:
    print("Unknown status code")
