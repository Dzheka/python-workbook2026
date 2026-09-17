http_status = int(input())

if 100 <= http_status <= 199:
    print("Informational")
elif 200 <= http_status <= 299:
    print("Success")
elif 300 <= http_status <= 399:
    print("Redirection")
elif 400 <= http_status <= 499:
    print("Client Error")
elif 500 <= http_status <= 599:
    print("Server Error")
else:
    print("Unknown status code")