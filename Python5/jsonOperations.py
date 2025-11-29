import json

#.json.loads() s is for string
#json.dumps()

json_str = '{"name" : "vineetha","isworking": true}'

print(json_str)

py_obj = json.loads(json_str)

print(type(py_obj))

#.loads function converts the javasacript variable into appriopriate python datatypes
#true -> True
#None -> null



new_py_obj = {
    "name" : "vineetha",
    "isworking" : True,
    "wfh" : None
}

js_obj = json.dumps(new_py_obj)
print(type(js_obj), js_obj)

#from reading files -> use read, load

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj),py_obj)

data_to_dump = {"collge" : "RGUKT", "Age":25, "Branch" : "ECE"}

with open("newdata.json","x") as d: 
    # json.dump(data_to_dump, d)
    json.dump(data_to_dump, d, indent=4, sort_keys=True)
