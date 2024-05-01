"""
data types in numpy arrays.:


in order to find the datatype of array we can use => dtype.
we can also change the data type of array by =>

for changing datatype of array we can use this shortcut in dtype
we can use just i for changing to integer, user b for changing to boolean
more example are given as.....

i   integer
b   boolean
u   unsigned integer
f   float
c   complex float
m   timedelta
M   datetime
O   object
S   string
U   unicode String




for changing data types we have multiple methods given below number wise.
ab1 = np.array([22, 43, 29, 50])

1) ab1 = np.array([22, 43, 29, 50], dtype = np.int8)
2) ab2 = np.float(ab1)  will change ab1 to float.
3) ab1 = np.array([22, 43, 29, 50], dtype = "f") will change it to float.
4) neww = ab1.astype(float)  by all these methods we can do change datatype.




"""

import numpy as np

abc = np.array([1, 2, 3])
print(abc.shape)
print(abc)

var = np.array([1, 3, 4, 5, 9])
print("data type : ", var.dtype)  # this will simply show the data type of the array.

floatabc = np.array([1.3, 4.2, 8.9])
print(floatabc.dtype)

# -----------------------------------------------------------------------------------------------------------

# if we want to change from one data type to any data type
# we can just use . and then its name
# np array have diff type of data types like int8 int32 int64 example.
# example give below.

print("changing daat type")
x = np.array([1, 4, 9, 19], dtype=np.int8)  # this will change any data type of array to int8
print(x.dtype)

print("changing daat type")
y = np.array([1, 4, 9, 19], dtype=np.int_)  # this will change any data type of array to int32
print(y.dtype)

# -----------------------------------------------------------------------------------------------------------
# we can also do this by shortcut.
# like for changing to int we can use just i
# for changing to boolean we can use b
# all the values are given above.

print("changing datatype short cutly")
y = np.array([1, 3, 99, 100, 38], dtype="f")
print(y.dtype)
print(y)
# -----------------------------------------------------------------------------------------------------------

# we can also use this conversion as a function like we can use
# float32(abc) and now this will change abc to float32.


ab1 = np.array([22, 43, 29, 50])
neww = np.float32(ab1)
newwww = np.str_(neww)

print("ab1 dataype", ab1.dtype)
print("neww data type", neww.dtype)

print("ab1 array : ", ab1)
print("neww array : ", neww)
# so just like this we can use these as a functions.

# just like this we can also change it to int or any other other datatype.

newwagain = np.int_(neww)
print("new again array : ", newwagain)
print("new again array data type : ", newwagain.dtype)
# -----------------------------------------------------------------------------------------------------------

# we can also convert this directly....
print("direct method.")
bb = np.array([33, 53, 89, 32])
new1 = bb.astype(float)  # this will change it to float.
new2 = bb.astype(str)   # this will change it to string.
print(bb.dtype)
print(new1.dtype)
print(bb)
print(new1)
print(new2.dtype)
# -----------------------------------------------------------------------------------------------------------
