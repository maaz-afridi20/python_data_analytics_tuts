"""
JOIN AND SPLIT FUNCTION :

JOIN :
join mein joining content of two or more arrays in single array.
but number of data(element) must be same for joining.


we can join array by using .concatenate() method.
there is also another method called => .stack()
this function will also join arrays. but it has its own parameters.


SPLIT :
just like for joining diff arrays we use a .concatenate() and .stack()
in splitting we split on array into many diff arrays.
we also have to mention that into how many arrays we have to split it.

we will use .array_split() function.
this will give us small array in list.
so now if we want to get the exact array not the list then we can use the indexing
like
print(arr[0])
so this will give the 1st array in that new list of smaller arrays.

"""
import numpy as np

# 1D Arrays.
var = np.array([1, 8, 9, 4])
var1 = np.array([5, 8, 98, 12])

arr = np.concatenate((var, var1))
print(arr)

# 2D Arrays.
"""
in 2D array we have to mention the axis that along which axis we want to merge 
"""
bb = np.array([[1,2],[3,4]])
bb1 = np.array([[5,6],[7,8]])
print(bb)

arrnew = np.concatenate((bb, bb1), axis=1)  # now this will concatenate both arrays
# along rows because we have mentioned axis=1
# we can also use axis=0 this will merge in columns.
print(arrnew)

# --------------------------------------------------------------------------------------------

# STACK FUNCTION...
"""
we can also use stack function for merging arrays like .concatenate()
in stack it has its own functions.
if we want to merge it according to rows then we can use hstack() mean horizontal stack
if we want to merge it according to colum then we can use vstack() mean vertical stack
if we want to merge it according to height then we can use dstack() 
we can also use axis function just like concatenate().
"""

bb11 = np.array([[1,2],[3,4]])
bb22 = np.array([[5,6],[7,8]])
print('old')
print(bb11)
print(bb22)
print('new')
arrnew22 = np.stack((bb, bb1),axis=0)
print(arrnew22)

# --------------------------------------------------------------------------------------------
# SPLIT FUNCTION(FOR SPLITTING ARRAYS)

vary = np.array([1, 8, 9, 4])
print(vary)
ary = np.array_split(vary, 2)  # this will split our main array into 2 smaller arrays
# because we have mentioned 2
# we can give any value instead or 2. into how many smaller array we want to split the
# main array that value we have to provide.
print(ary)

bbc = np.array([[1,2],[3,4]])
print(bb.ndim)
print()
arree = np.array_split(bb, 2, axis=0)


# --------------------------------------------------------------------------------------------
# bb = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(bb)
# print("dim : ", bb.ndim)
# print("Shape : ", bb.shape)
# arr = np.array_split(bb, 2)
# print()
# print(arr)
# print("dim : ", bb.ndim)
# print("Shape : ", bb.shape)
# print(type(arr))
# print()
# print(arr[0])
