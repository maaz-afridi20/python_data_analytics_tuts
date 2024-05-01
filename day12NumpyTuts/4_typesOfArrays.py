"""
Array can be of 1D, 2D, 3D
and also more than this.


1D => the 1D array can be seen like this [1 3 5 1 9 0]
2D => in 2D it has two square brackets like   [[1 89 249 29]]
3D => while in this it has 3 [[[]]]    =>  [[[14 7 98 48]]]


if we want to find that how many dimensional array is this than we can use
ndim() function this will give you the number of dimensions of that array.

"""
import numpy as np

yy = np.array([[1, 2, 4, 1]])
yyy = np.array([[[4, 9, 48, 1]]])
check = np.ndim(yy)
check2 = np.ndim(yyy)
print(check)
print(check2)

#  we can also use like this.
abc = yy.ndim
abccc = yyy.ndim

print(abc)
print(abccc)
# and also like this.
print("again", yyy.ndim)

ar2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
checkar2 = ar2.ndim
print(checkar2)
print(ar2)


arrr = np.array([[1, 2, 4]])
print(arrr.ndim)


# below is 3D array.
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(arr3)
print(arr3.ndim)


# if we want to create more than 3 or 4 D array we can use ndmin function and specify the
# dimension this will create that much of dimension of array.

arn = np.array([1, 2, 3, 4], ndmin=10)  # this will create 10D array
print(arn.ndim)
print(arn)

