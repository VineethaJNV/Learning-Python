import os

s = open("temp.txt","x")
s.close()
os.remove("temp.txt")