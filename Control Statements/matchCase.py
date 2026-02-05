# switch case in python.
status_code = 200
match status_code:
    case 200:
        print("Status Okay!")
    case 404:
        print("Not Found!")
    case _:
        print("Invalid")