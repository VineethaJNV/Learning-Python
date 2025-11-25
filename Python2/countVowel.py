vowels="aeiou"

count = 0

word = "vineetha"

for ch in vowels:
    if(ch in word):
        count+=1

print("vowel count : ", count)