l = [0,1,4,9,16,25]

#achieve the above wiht loop
squares=[]
for i in range(0,6):
    squares.append(i*i)

print(squares)

#with list comprehension
#output iterating variable, range, condition if needed
sq = [i*i for i in range(6)]
print(sq)

#squares of only odd numbers


odd_sq = [i*i for i in range(6) if (i%2 ==1)]
print(odd_sq)


#[-2, -4, 3, 5, 2, -1] -> [0, 0, 3, 5, 2, -0]
arr = [-2, -4, 3, 5, 2, -1]
neg_removed_list = [i if(i>0) else 0 for i in arr ]
print(neg_removed_list)

words = ["Vineetha", "Varshitha", "vasavi"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

lowercase_words = [word.lower() for word in uppercase_words]
print(lowercase_words)