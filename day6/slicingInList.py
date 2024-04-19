"""
Slicing In List :

"""

fruits = ["apple", "mango", "banana", 1, 14.0]
print(fruits[0])
print(fruits[0][:2])

# just like string slicing we can also use negative slicing
print(fruits[-1])   # this will print 14.0
print(fruits[:3])
print(fruits[:2])

# for giving some gaps.

print(fruits[::2])  # this will print all the values while skipping 2 values after every value.

# for finding the reverse of any list we can use -1 just like string...

print(fruits[::-1])  # this will reverse the list.


print(fruits[-1:-4:-1])

