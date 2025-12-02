#new_words_dictWriteaprogramthattakesastringfromtheuserandprintsthenumberofspacesinthestring.
def calc_spaces_in_string(string_to_calc_spaces):
    count = 0
    for char in string_to_calc_spaces:
        if(char ==" "):
            count +=1
    return count

sentence = input("Enter string to count spaces : ")
print(f"the number of spaces in {sentence} are {calc_spaces_in_string(sentence)}")