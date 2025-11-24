user = "admin"
password = "pass"

u = input("Enter username")
p = input("Enter password")

if(user == u and p == password):
    print("login successful")
elif(user == u):
    print("invalid password")
else:
    print("invalid username")