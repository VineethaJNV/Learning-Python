

def print_positive_or_negative():
    while(True):
        ip = input("Enter your input : ")
        if(ip == 'QUIT' or ip == 'quit'):
            return
        else:
            if(int(ip) > 0):
                print(f"Given number {int(ip)} is positive")
            else:
                print(f"Given number {int(ip)} is negative")

print_positive_or_negative()