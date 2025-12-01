#print the digits of a number

num = int(input("Enter the number to print its digit"))
while(num > 0):
    rem = num % 10
    print(rem)
    num = num//10