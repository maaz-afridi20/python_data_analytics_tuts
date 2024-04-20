
employee_data = {"name": "ali", "age": 40, "gender": "male"}

for i in employee_data:     # this will print all the keys
    print(i)


for x in employee_data:     # this will print all the values.
    print(employee_data[x])

"""
for printing single value from dict we use employee_data["keyName"]
this will print the value of the key. 
so if we use the loop just like above in the print statement
we give the x because when the value iterate that value stores in x
so that is why when we use employee_data[x] we used x so when the
value iterate it will print that values. 
"""

# using value function for getting values.

for ii in employee_data.values():  # this will print all the values directly
    print(ii)

for vv in employee_data.keys():  # this will print all the keys. directly
    print(vv)


# if we want to print keys we can use .keys() method.

employeeDataKeys = employee_data.keys()
print(employeeDataKeys)

employeeDataValues = employee_data.values()
print(employeeDataValues)
print("-"*60)
print(employee_data.items())  # this will print all the keys and values at a time.

# we can also iterate using loops.

for i, y in employee_data.items():
    print(i, " : ", y)

