"""
List Functions :

.len() => finds length
.count() => for counting occurrence of something
.append() => to add something in the end of the list.
.insert() => to add something in the list in some specific place.
.remove() => to remove something.
.pop() => we use this method for removing if we do not know the exact object
         in the pop we only give index number

.copy() => to create a copy of list.
.index() => if we want to find the index of some value.
            print(fruits.index("banana")) this will print the index of banana on which index banana is
.extend() => to extend(add) some values more than one
.reverse() => to reverse list.
.sort() => arranging some list alphabatically or numberwise
.clear() -> this will clear all the things from list.
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


SecondFruits = fruits.copy()
print(SecondFruits)


print(fruits.index("banana"))  # this will print the index of banana on which index banana is

c = ["vision", "element of c"]
fruits.extend(c)
print(fruits)
print(fruits.reverse())


c.sort()    # this will sort list c alphabatically
print(c)

d = [1, 5, 3, 75, 9, 46]
d.sort()
print(d)


d.clear()
print(d)
