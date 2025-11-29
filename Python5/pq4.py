import json
py_dict = {"bangalore" : 100000000, "hyderabad" : 10000000, "Chennai" : 1000000}

with open("cities.json","x") as f:
    json.dump(py_dict, f)

    city = input("enter city name : ")
    population = int(input("enter population"))

    new_dict= {city:population}
    json.dump(new_dict, f)
