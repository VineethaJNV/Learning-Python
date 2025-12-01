#Sum of digits of a number

def calc_sum_digits(num):
    sum = 0
    while(num > 0):
        sum += num%10
        num = num//10
    return sum

num = int(input("Enter number to calculate the sum of its digits"))
print(f"The sum of digits of{num} is : {calc_sum_digits(num)}")