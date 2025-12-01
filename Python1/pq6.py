val1 = int(input("Enter number"))
val2 = int(input("Enter another number"))

print(f"before swapping : {val1} and {val2}")
#swap the numbers
temp = val1
val1 = val2
val2 = temp
print(f"After swapping : {val1} and {val2}")
