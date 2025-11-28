with open("wordSearch.txt", "r") as f:

# data = f.read()

    word_to_search = "Python"
    count = 0
    while(f != None):
        line = f.readline()
        count+=1
        if(word_to_search in line):
            print(f"{word_to_search} is found in line number {count}")
