#given a tuple of integers, create a tuple of all even numbers and all odd numbers

tup = tuple(map(int, input("Enter the integers : ").split()))

even_tup = []
odd_tup =[]
for num in tup:
    if(num%2 == 0):
        even_tup.append(num)
    else:
        odd_tup.append(num)

print(tuple(even_tup), tuple(odd_tup))