"""
Shapes and Reshape :

when we create an array if we want to find the shape of an array
then we can use the .shape method to find the shape of the array like
how many rows and how many columns etc.
when we create an array like
aa = np.array([[1,2],[1,2]])
so in maths this mean like this

 ____    ___
| 1    2   |
|         |
|1     2 |
|___  ___|

this is just a matrix like this.



==> now in order to reshape our array we can use .reshape function.

"""
import numpy as np

aa = np.array([[1, 2], [1, 2]])
print(aa)
print(aa.ndim)

# if we want to find the shape of array

print(aa.shape)

ab = np.array([[1, 2, 3, 4], [1, 3, 4, 9]])
print(ab.shape)

var1 = np.array([3, 4, 9, 33], ndmin=4)  # this will create 4D array
print(var1)
print(var1.ndim)
print(var1.shape)

#  if we want to reshape the array like if we have an already created array
# and we want to reshape it lie from 1D to any multi D
# we can also do this... by reshape.

aba = np.array([4, 99, 38, 189, 88, 199])
print(aba.shape)
print(aba.ndim)

# so in the reshape function we have to define 2 arguments
# like in reshape we have to give in first place that how many rows we want
# and in second place we have to give number of columns.
xx = aba.reshape(3, 2)  # this will change shape of aba array to 3, 2
print(xx)
print(xx.shape)

# we have created a 2D array now if we want to create 1D array from 2D then we can use this.
# we can use again the reshape....
# so if we use (-1) in reshape then it will change it back to again 1D array.

xxnew = xx.reshape(-1)  # this will change that array to 1D again...
print(xxnew)
print(xxnew.shape)
print(xxnew.ndim)


# so just by putting -1 in reshape it will change that array again
# to simple 1D array
