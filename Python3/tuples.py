tuples = (1, 2, 3, 4, "vinee", "veera", "jnv", 10.0, 56)
#tuples are immutable

print(len(tuples))
# print(tuples.get(0))

for t in tuples:
    print(t)

sample_tuple = (1) #won't be considered as tuple
print(type(sample_tuple))
