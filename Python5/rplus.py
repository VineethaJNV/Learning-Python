f = open("sample.txt","r+")

data = f.read()

print(data)

f.write("checking the r+ mode")

data = f.read()

print(data)

f.close()

