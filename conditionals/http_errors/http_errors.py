status = int(input ())
if status >= 100 and status <= 199:
    print ("Informational")
elif status >= 200 and status <=299:
    print ("Success")
elif status >= 300 and status <= 399:
    print ("Redirection")
elif status >= 400 and status <= 499:
    print ("Client Error")
elif status >= 500 and status <= 599:
    print ("Server Error")
else: 
    print ("Unknown status code")