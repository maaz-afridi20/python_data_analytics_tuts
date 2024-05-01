"""
how to create numpy array :
by the np.array() function this will create the array
"""

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

# we can also do like this.
x = [2, 4, 6, 8, 10]

y = np.array(x)
print(y)
print(type(y))

# simply the .array() function will change any list or thing to array.

l = []
for i in range(1, 5):
    value1 = int(input("Enter Value : "))
    l.append(value1)

print(np.array(l))

