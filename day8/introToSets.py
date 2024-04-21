"""
Sets :
👉 unordered collection of data.
👉 unlike in the list, tuple, or dictionaries all the items are in ordered and have a indexes.
👉 while in the sets there is no order in sets.
👉 when we print any value it will print the value in diff order.
👉 sets are written in {}
👉 they are mutable we can change the values, like delete, add , remove etc.
👉 values are separated by ,
👉 all the values will be unique. like if we have same value more than once then
    it will not be printed.

"""

a = {1, 12, 78, 23, 12}
print(type(a))
print(a)

b = {"ironman", "hulk", "thor", "captain", "spider man", 8}
print(type(b))
print(b)

for i in b:
    print(i)
