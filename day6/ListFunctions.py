"""
List Functions :

len() => finds length
count() => for counting occurrence of something
append() => to add something in the end of the list.
insert() => to add something in the list in some specific place.
remove() => to remove something.
pop() => we use this method for removing if we do not know the exact object
         in the pop we only give index number
"""

fruits = ["apple", "mango", "banana", "grapes", 49, 8.2, "mango"]
print(len(fruits))

print(fruits.count("mango"))

fruits.append("last")
print(fruits)

# we can also use the negative index.
fruits.insert(3, "Indexed")     # now the indexed word will be added at 3rd index.
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.pop(-1)  # remove the object using indexing.
print(fruits)
