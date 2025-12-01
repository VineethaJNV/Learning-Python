salary = float(input("Enter your salary to calculate tax with the given conditons"))
final_tax = 0
if(salary < 30000):
    final_tax = (salary*(5/100))
elif ((salary > 30000) and (salary < 70000)):
    final_tax = (salary*(15/100))
elif salary > 70000:
    final_tax = (salary*(25/100))
print(f"the final tax for the given income of{salary} if {final_tax}")