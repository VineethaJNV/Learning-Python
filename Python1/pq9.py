principal = float(input("Enter principal amount : "))
rate = float(input("Enter rate of interest"))
time = float(input("Enter the time in years"))

simple_interest = (principal * time *rate)/100

print(f"The simple interest for an principal of { principal} wiht an interest rate of {rate} for a time period of{time} is {simple_interest}")