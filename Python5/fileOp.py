f = open("sample.txt", "r") #returns file object


rl = f.readline()

print(rl)

data = f.read()
print(type(data))

print(data)

rl = f.readline()

print(rl)



f.close()

w = open("sample.txt", "w")
w.write("writing for demo") #overwrites the file



