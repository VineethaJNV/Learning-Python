start = int(input("Enter the starting range to print the even numbers from : "))
stop = int(input("Enter the ending range to print the even numbers to : "))

for num in range(start, stop, 1):
    if(num % 2 == 0):
        print(num)