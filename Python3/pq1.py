#is palindrome

def is_palindrome(name):
    for i in range(len(name)//2):
        if(name[i] != name[len(name)-i-1]):
            return False

    return True

name = input("Enter input to check if it is a palindrome : ")
if(is_palindrome(name)):
    print(f"The given string {name} is a palindrome")
else:
    print(f"The given string {name} is not a palindrome")

