try:
    with open("data.txt" ,"r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
else:
    print("file is present")
finally:
    print("operating on file")