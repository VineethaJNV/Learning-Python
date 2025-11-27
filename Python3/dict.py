dict_sample = {1 : 2, 2 : 3, 4:5, "vinee" : 3, "veera:":5}

for items in dict_sample:
    print(dict_sample.get(items))

dict_sample["reddy"] = 11
print(dict_sample)