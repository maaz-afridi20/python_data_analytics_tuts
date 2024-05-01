"""
Shuffle: just like to shuffle anything we use shuffle
         if we want to shuffle data in any array we can use
         shuffle method.
         for this we can use np.random.shuffle(array)
         this will shuffle the data of the array.
Unique:  in order to find some unique value in array we can use
         unique parameter. this will find the unique value inside the array.
         this also have some other parameters like finding the index of that value etc.
Resize:  if we want to resize any array we can use function method.
Flatten: both the flatten and the ravel is used for changing 2D array to 1D

Ravel:

"""

import numpy as np

# ----------------------------------------------------------------------
# SHUFFLE
kk = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.random.shuffle(kk)
print(kk)

# ----------------------------------------------------------------------
# UNIQUE

kk = np.array([3, 2, 3, 2, 5, 6, 2, 8, 2, 3])
x = np.unique(kk, return_index=True, return_counts=True)  # if we use return index = true
                                      # this will also give use the index number of that
                                      # unique values
                                      # we have return count true which mean this will also give us
                                      # number of times that value repeats will also be show
                                      # if we write return_count_True


print(x)

# this will give us unique value mean not repeatative values.
# ----------------------------------------------------------------------
# RESIZE :

kk = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.resize(kk,(3,3))
print(y)
# iss resize mein hm nay array dii hai k jiss ko resize krna hai...
# orr uss k sath mein number of rows and columns b dii hain k jo new array ho
# uss ki shape kaisee ho... to wo hm nay mention kii hai k 3by3 ho...

# ----------------------------------------------------------------------
# Flatten
#
# you can also some optional parameter which is "C","F","A","K"
# like this...
# print(abb.flatten(order="F"))
# through this order parameter it will change the style of rows and columns.
abb = np.array(([[1,3],[3, 4]]))
print(abb.flatten())

# ----------------------------------------------------------------------
# Ravel
#
