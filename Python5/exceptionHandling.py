#try, except, else, finally

try:
    x = int(input("enter num"))
    ans = x/0
except ZeroDivisionError:
    print(f"Division by 0 is not allowed")

except ValueError:
    print(f"Division by 0 is not allowed")
else:
    print(f"ans is {ans}")
finally:
    print("End of program") #Will be executed irrespective of error being thrown or not