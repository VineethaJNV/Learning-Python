n = int(input("Enter number to calc factorial"))

result = 1

for i in range (1,n+1):
    result*=i
print(result)