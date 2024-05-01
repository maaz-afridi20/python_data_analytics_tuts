"""
Difference between list and numpy:

in list, we can store diff type of datatypes like example below
list = [1, 3, "this", 5.0, true]
while in numpy we have to use only single datatype.

👉  list is inbuilt module
    while for numpy we have to install numpy module

👉 list have less efficiency for numerical operation
   while numpy have good efficiency in this.

👉   list is single dimensional
     numpy array can b multidimensional
     in image processing the numpy is very handy

    numpy is convenient to use.

one of the main diff is that list cannot handle direct mathematical operations
like addition, subtraction etc.
while in array we can do it easily.

we can also find out the time of the execution of any code like
if we create list we can find the time out of creating list
so in this case the time taken for creating simple list is more
while the numpy array takes less time.
mean its time efficient.

for finding out the time of any code execution we can use =>  %timeit
now this will only give you the time taken of only single line of code
in which it is written. while if we want to find out the time take of the whole code
then we can use =>      %%timeit

we have to use double %% then this will give us the time taken of whole code(program).

this will give you the time of execution.

example...
"""
# import numpy as np
#
# %timeit [j**4 for j in range(1, 9)]
#
# %timeit np.arange(1, 9)

# the arrange funtion will create an array with the starting point and the ending point.
# this will also act as range function.

# so this will give you the time taken by both of the function.
# and you will see that np will take less time.
