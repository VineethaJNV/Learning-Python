with open("logs.txt","a") as f:
    f.write("Program is running successfully!")
    f.close()

with open("logs.txt", "r") as r:
    data = r.read()
    lines = data.split("\n")
    for line in lines:
        print(line)