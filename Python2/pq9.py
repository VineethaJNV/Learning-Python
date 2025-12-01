

def is_prime(num):
    for n in range(2, num-1):
        if(num % n == 0):
            return False
        
    return True

num = int(input("Enter number to check if it is prime or not"))
if(is_prime(num)):
    print(f"the given num {num} is prime")
else:
    print(f"the given num {num} is not a prime")
    