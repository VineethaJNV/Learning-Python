#Create  adictionary that maps each word to its length

words =["apple","banana","kiwi","cherry","mango"]

new_words_dict={}

for word in words:
    new_words_dict[word] = len(word)

print(new_words_dict)