http = float(input())

if http >= 100 and http <= 199:
    print("Informational")
elif http >= 200 and http <= 299:
    print("Success")
elif http >= 300 and http <= 399:
    print("Redirection")
elif http >= 400 and http <= 499:
    print("Client Error")
elif http >= 500 and http <= 599:
    print("Server Error")
else:
    print("Unknown status code")