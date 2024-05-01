"""
Special type of array(filled with specific value)

Array filled with 0's => we can create this by using .zeros(number of zeros) function
Array filled with 1's => could be created with the help of .ones() function
Create an empty array => with the help of .empty()
An array with range of element => with the help of np.arange(1,9) // just like range function
An array with the diagonal element filled with 1's => with the help of np.eye(rowBycolumn)
An array with some spacing => np.linspace(start, end, num=5)
"""

import numpy as np

# -----------------------------------------------------------------------------------------------------
# creating array with 0's
arr_zero = np.zeros(4)  # this will have 4 zeros in array.
                        # this will be 1D array.
print(arr_zero)
print(type(arr_zero))


# we can also specify number of dimensions to have 0's like if we want the array
# to be multidimensional and having all the elements zero we can also do this. like
print("zeros check.")
arr_zero1 = np.zeros((2, 3))  # this will have 2 rows and 3 columns.
# but element will be all 0's
print(arr_zero1)
print("dim of zerors check : ", arr_zero1.ndim)

# now the 2 is showing the dimensions of array, while the 3 is showing that how much zeros will
# be there in them. so it will have 2 dimension and all the elements wille be zero.

print("checkkk")
arrzero2 = np.zeros((3, 5))  # this array will have 3 rows and 5 columns mean 3by5 array.
# but all the element will be 0
print(arrzero2)

# -----------------------------------------------------------------------------------------------------
# creating array with 1's


ones1 = np.ones(4)  # all the element will be 1's. this array will be 1D
print(ones1)

ones2 = np.ones((2, 5))  # this will be 2D array and all the element will be 1's
                         # having 5 ones in every row.
                         # it will have 2 rows and 5 columns.

print(ones2)
print(type(ones2))

# -----------------------------------------------------------------------------------------------------
# creating empty array

emt_array = np.empty(5)  # this will empty array the 5 shows that how many columns will have only
print(emt_array)

# -----------------------------------------------------------------------------------------------------
# creating array with range of values.

# we can do this by the use of .arange() function

arrRange = np.arange(4)  # this will add values in array from 0 to 4
# this works just like a range function in simple py.
print(arrRange)

arrRange2 = np.arange(1, 8)  # this will add values in array from 1 to 7
print(arrRange2)

# -----------------------------------------------------------------------------------------------------
# creating array of all the diagonal element with 1
print("diagonal array with 1 ")
arrdiag = np.eye(3)  # this will create 3by3 array having all the diagonal element = 1
# array is 2D
print(arrdiag)

# if we want to create our custom array then we can also use this.

arrdiag2 = np.eye(3, 5)  # this will create an array of 3 by 5
# rows will be 3 and columns will be 5
# but the array will be 2D
# and all the elements of diagonal will be 1
print(arrdiag2)

# -----------------------------------------------------------------------------------------------------
# creating array with some specific spacing.

arrlin = np.linspace(0, 20, num=5)
print(arrlin)

# like by this it will give us 1D array
# and the first element will start from 0 and the last element will be 20
# now the total elements will be 5
# because we have mentioned num=5
# so this will be happened that
# k number 0 say start hoga orr end hoga 20 pr hm nay mention kiyaa hai k humein
# chahiyee siraf 5 elements tu ye aisa karega k iss ko spacing dega khud say
# matlab k pahla element lega 0, phir lega 5 phir lega 10, phir lega 15 phir 20
# tu iss tarah ye 0 say start ho kr 20 tk b chala jaye ga orr siraf 5 elements
# b ajayengay ... agar hmm iss type k kuch krna chahtay hain tu hm ye linspace ka function
# ko use kr sktay hain......

arrlin2 = np.linspace(1, 21, num=4)
print(arrlin2)

# bss ye khud say 4 number ko manage karay ga... from 1 to 21.. bss uss ko divide karega.. k konsii
# value aye gii.. magar ye siraf 4 number ko hii laye ga array mein...




