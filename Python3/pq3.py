l1 = list(map(int, input("Enter the elements of first list").split()))
l2 = list(map(int, input("Enter the elements of second list").split()))
for n in l2:
    l1.append(n)

l1.sort()
print(l1)