"""
a dictionaries is a key value pairs.
for declaring dictionaries we use {}
syntax is =>  dict_name = {"key":value, "key":value ..... }
each key value pair must be separated by :
it does not have items with same keys.
so if we have 2 value with same keys then the key which is coming later will be save
in that dict.
Dictionaries are mutable ;

if we want to get some specific value we do not use indexing instead we use
the key of that thing, and we get the value of that.

"""

car = {"brand": "audi", "model": "q7", "price": 4778823}
print(type(car))
print(car)

car["model"] = "q8"  # this will change the value of model from q7 to q8.
print(car)
print(len(car))  # will print the length of key value pair of dict.

print(car["model"])
print(car["brand"])

print(car.keys())
print(car.values())

employee_data = {"name": "ali", "age": 40, "gender": "male"}
print(employee_data)

print(employee_data["name"])
print(employee_data["age"])
