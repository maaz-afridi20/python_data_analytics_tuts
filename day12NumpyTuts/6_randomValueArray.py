"""
Creating an array with random values.
this can be done by 4 methods. given below.

1) rand() => helps to generate random value from 0 to 1 (only positive values)
2 randn() => help to use to generate a random value closer to 0. it may be negative or positive
3 ranf() => this function will also generate values from 0 to 1 but 1 will not be included
            while 0 will be included... it can be shown as  [0.0 ,1.0)
            it mean that 1 is not include while 0 is included.
4 randint() => this function use to generate a random value between some specific given range.
"""

import numpy as np

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

print("rand function")
arrrnd = np.random.rand(5)  # this will create 1D array of 5 values in between from 0 to 1 (1D array)
arrrnd2 = np.random.rand(10)  # will create 1D array of 10 values in between from 0 to 1 (1D array)
print(arrrnd)
print(arrrnd2)

print("******")
# if we want to create 2D or more dimensional array we can use like this.
arrrnd3 = np.random.rand(4, 3)  # this will create array of 4by3 (dimension will be 2D array)
print(arrrnd3)
print(arrrnd3.ndim)  # wil show dimensions of array
print("******")


# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


print("randn function")
arrrandn = np.random.randn(5)  # this will create 1D array of 5 values closer to 0
arrrandn2 = np.random.randn(2)  # this will create 1D array of 5 values closer to 0
                                # values can be negative
                                # only when we use randn function. (not in rand)
print(arrrandn)
print(arrrandn2)

print("******")
# creating more than 1D array
arrrnd3 = np.random.randn(4, 2)  # this will create 2D array.
print(arrrnd3)
print(arrrnd3.ndim)


# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

print('ranf function')
arrranf = np.random.ranf(4)  #
arrranf2 = np.random.ranf(8)
print(arrranf2)
print(arrranf)

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
print('generating random values bw some specific range..')

arrrandint = np.random.randint(1, 10, size=5)  # this will create any 5 random value from
# 1 to 10
print(arrrandint)

bb = np.random.randint(1, 11, size=10)

