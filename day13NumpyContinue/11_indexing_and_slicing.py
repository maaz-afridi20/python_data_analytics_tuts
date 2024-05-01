"""
INDEXING and SLICING....:

just like list it's values has indexing
and also it has negative indexing.

now if we have 2D array, and we want to find the indexes
the whole first row will act as 0, the next whole row will be 1
so now in 1D Array single elements will have 0, or 1 or 2 indexing while in
2D arrays the whole rows will act as 0 or 1 and so on.


SLICING :
slicing just mean that if we want some multiple values like
[1, 2, 3, 4, 5, 8, 9]
like if we want values from 2 to 8
this is called slicing.



"""

import numpy as np

print('this is for 1D array')
var = np.array([1, 8, 18, 4])
print(var[0])  # this will give us 1
print(var[-1])  # this will give 4
# ----------------------------------------------------------------------------
print('this is for 2D array')

var2 = np.array([[9, 3, 99], [7, 5, 10]])
print(var2)
print(var2.ndim)
print(var2.shape)

# now for getting values in 2D array here is the way...
print('getting index values from 2D')
print(var2[0][1])  # so now the 0 mean first row, and now after this 1 mean that
# in the first row give me second element so now this will give us 3
print(var2[1][2])  # this will give us 10
# because we have mentioned that from the second row because we have mentioned 1
# and then in the second row we want 3rd element that's why we use 2 because
# indexing start from 0

# we can also do like this.
print(var2[0, 0])  # this will work same like print(var[0][0])
print(var2[1, 1])  # this will work like print(var[1, 1])


# ----------------------------------------------------------------------------
print('this is for 3D array')
var2 = np.array([[[9, 3, 99], [8, 39, 2], [10, 88, 44]]])
print(var2[0][0][0])
print(var2[0, 0, 0])  # this will also work same like print(var2[0][0][0])
# this will give us 9
# same concept like above for 2D array.
# ----------------------------------------------------------------------------
print('..........SLICING.......')
#
print('for 1D Array....')
abc = np.array([1, 8, 8, 18, 4, 18, 100, 48, 32, 24, 98, 135, 4, 88, 00, 82])
print(abc[0:5])

# we can also specify steps like how much steps we want to jump
abc2 = np.array([1, 8, 8, 18, 4, 18, 100, 48, 32, 24, 98, 135, 4, 88, 82])
print(abc[0: 11: 2])  # the last 2 mean that we want to jump 1, mean skip 1 value and then
# goto next.

# if we want to start slicing from some value and goto end
# we can use like this
# print(abc[0:]) so this mean that start from 0 and goto ent
# we did not specify the end it meant we don't know the end
# we want all values to end.
print(abc2[3:])
# and also we can do this like if you want to start from starting value
# then we also do this.
print(abc2[:6])  # so this will start from starting value and goto index number 6
# if we write simply this print(abc[::2])
# this would mean that go from start to end and jump 1 value

# ----------------------------------------------------------------------------
print('....SLICING.......')
print('for 2D Array....')

# for 2D arrays we have to do indexing first like above and then mention the slicing...
kkk = np.array([[9, 3, 99, 18, 100, 48, 32], [7, 5, 10, 2, 3, 4, 5]])
print(kkk[0, 0:2:2])
# all other concepts are same for slicing... like steps, or going from start to end etc.
# just you have to do the indexing like the above 2D or 3D in the first parameter
# and then you can do... any thing.
