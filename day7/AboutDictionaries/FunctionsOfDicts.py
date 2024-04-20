# functions of dicts.
"""
.items() print key and value both
.get() get any key
.keys() print keys
.values() print values
.copy()  create a copy of whole dict.
.update()
.setDefault("key", "value")  this will check if the key value pair exits then it will update this
                or if there is not that key value pair then this will add that
                key value instead.

.pop("keyName")  it will remove that value from dict.
.popItem()  this will remove any of the item from the dict even you don't know the key and value.
            example given below.
            you don't have to give the key to delete. it will automatically delete
            the last item from dict.
.clear()
"""

student = {"name": "john", "class": "5th", "roll": 49}
print(type(student))

# get
# it give us the value of any key
x = student.get("name")  # will print the value of name.
y = student.get("roll")  # will print the value of roll no.
print(x)
print(y)

# we can also get the value of any key using this below method.
z = student["class"]
print(z)


itemsOfStudent = student.items()
print(itemsOfStudent)


keysOfStudent = student.keys()
print(keysOfStudent)

valuesOfStudent = student.values()
print(valuesOfStudent)


newDict = student.copy()    # will copy whole student dict in another dict.
print(newDict)

print("_"*60)
print(newDict)

newDict.pop("roll")  # this will remove roll from newDict dict.
print(newDict)


poppedItem = newDict.popitem()
print(poppedItem)
print(newDict)


newDict.setdefault('age', 78)  # now ye check karege k age key hai k nai. agar ye key haii tu uss ki
# ye value ko change to 78 kr dega orr agar ye age wali koii key ho hii naii tu ye
# khud ba khud hii add kr dega age ki key ko b orr age ki value ko b
print(newDict)

