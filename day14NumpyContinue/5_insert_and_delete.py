"""
Insert And Delete :

Insert:     for inserting some value inside array we can use insert function.
            so in insert function there is 3 parameters. on first position
            we have to give the array in which we want to insert
            in second position we have to give the index where we want to
            insert that value.
            in third, we want to put that value which we want to upload. like eg below.
            it only adds int value not a float value.
            we can also use .append() just like simple lists.
            with the help of append we can also add float values.
"""

import numpy as np

# --------------------------------------------------------------------------------------
vv = np.array([1, 5, 29, 89, 100])
print(vv)
v = np.insert(vv, 2, 50)
print(v)

# we can also give a whole (index values. ), like more than one value to insert at some place.
bb = np.array([10, 20, 30, 35, 60, 80])
bbcc = np.insert(bb, (0, 2, 3), 40)
print(bbcc)
# so this will put 40 at 0 index and 2nd index and 3rd index
#
# working with 2D array...
# in 2d we have to also mention the axis.
kkk = np.array([[1, 2], [3, 4]])
kkk2 = np.insert(kkk, 2, 100, axis=1)
# if we want to insert multiple data we can use []
# like this
# kkk2 = np.insert(kkk, 2, [100, 200, 892,291], axis=1)
# --------------------------------------------------------------------------------------
#
# Delete
#
#

aa = np.array([1, 5, 29, 89, 100])
print(aa)
vc = np.delete(aa, 1)  # this will delete 1st index value from aa array.
print(vc)

