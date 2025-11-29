with open("names.txt","w") as f:
    for i in range(5):
        name = input("Enter name: \n")
        f.write(name)
        f.write("\n")
f.close()
with open("names.txt", "r") as r:
    data = r.read()
    print(data.split("\n"))