with open("wordSearch.txt", "r") as f:
    word_to_search = "python"
    count = 0
    data = f.read()
    lines = data.split(" ")
    for line in lines:
        count+=1
        if word_to_search in line:
            print(f"{word_to_search} exists in the file on line number{count}")