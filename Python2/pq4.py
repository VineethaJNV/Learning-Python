#write a function to return the count of the digits of given number

def count_digits(num):
    count = 0
    while(num > 0):
        rem = num %10
        count+=1
        num = num //10
    return count

num = int(input("Enter a number to count the number of digits inside it : "))
print(f"The number of digits inside {num} are : {count_digits(num)}")