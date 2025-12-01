#all numbers form 1 to 100 divisible by 3 and 5

def print_num(start, stop):
    for num in range(start, stop, 1):
        if(num % 5 == 0 and num % 3 == 0):
            print(num)

start = 1
stop = 100

print(f"the number b/w {start} and {stop} that are divisible by 3 & 5 are {print_num(start, stop)}")