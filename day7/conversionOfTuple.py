"""
some time we want to add something to tuple, but we cannot add
things to the tuple through function just like lists
so for this we first convert tuple to list then we can apply the addition function of list
to add something to tuple.
after converting to list now we can apply any function of list
to that converted tuple.
just like converting to list we can also again re convert it to tuple.
"""

a = ("oneplus", "nokia", "samsung")
print(type(a))
a = list(a)
print(a)
a.append("iphone")
print(a)
print(type(a))

a = tuple(a)
print(type(a))
print(a)

print(a.count("iphone"))    # this will count that how much time iphone is listed there in tuple.
print(a.index("oneplus"))   # will print on which index is oneplus

