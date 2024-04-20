
nestedDict = {"name": "ali", "age": 10, "subjects": {"physics": "yes", "maths": "yes", "chemistry": "no"}, "roll": 19}
print(nestedDict)

print(nestedDict.keys())


# nested dictionaries...
employee = {
    1: {"name": "ali", "age": 10, "gender": "male"},
    2: {"name": "khan", "age": 20, "gender": "female"},
    3: {"name": "cop", "age": 18, "gender": "female"}
}

print(type(employee))
print(employee)

# print(employee.get(1))
# print(employee.get(2))
print("_"*70)
# print(employee.get(1)["age"])

# we can also use this....

print(employee[1]["gender"])
# this will print the gender of the dict inside the first dict.


