username = input("Enter username : ")
password = input("Enter password : ")

if(username == "admin" and password == "pass"):
    print("Login successful!")
else:
    if(username != "admin"):
        print("invalid username")

    else:
        print("invalid password")
