a = open("sample.txt","a")

a.write("\nchecking if the data can be appended into the file") #appends in the same line, if needed in next line, add /n

a.close()

r = open("sample.txt", "r")

data = r.read()

print(data)
