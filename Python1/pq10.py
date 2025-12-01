num = input("Enter decimal number")

integer_fractionalpart = num.split(".")
print(integer_fractionalpart)

print(f"integer part in {num} is {integer_fractionalpart[0] }")
print(f"decimal part in {num} is {integer_fractionalpart[1] }")