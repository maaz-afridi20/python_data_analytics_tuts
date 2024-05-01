"""
Arithmetic Operations...

1) a+b, addition =>  np.add(a,b)
2) a-b, subtraction  => np.subtract(a,b)
3) a*b, multiplication => np.multiply(a,b)
4) a/b, divide => np.divide(a,b)
5) a%b modulus => np.mod(a,b)
6) a**b power => np.pow(a,b)
7) 1/a reciprocal => np.reciprocal(a,b)
8) for finding minimum => np.min(value)
9) for finding max => np.max(value)
10) for square root => np.sqrt(value)
11) for sin => np.sin(value)
12) for cos => np.cos(value)
13) for cumulative sum => np.cumsum(value)
    for cumulative product => np.cumprod(value)
14) for finding the position of the min or max value => np.argmax(value), np,argmin(value)

if we also want to find the position of the min or max value then we can also use
(argmin) value. just like this...  np.argmax(ll)
now this will give the  position of the max value which is in the ll array...
np.argmin(ll) now this will give the  position of the min value which is in the ll array...
like example below.


"""
import numpy as np

var1 = np.array([1, 88, 40, 99])
var2 = np.array([89, 93, 4, 51])
print(var1)
print(var2)

varadd = var1 + 3  # this will add 3 to all the values inside the array.
print(varadd)
# but this addition will be done with the single element of array
# if we want to add whole one array with other array then we can use np.addition(a,b)


wholearradd = np.add(var1, var2)
print(wholearradd)

# just like above when we add the whole array elements with 3 we can also do this in this add
# function like this...
# abccc = np.add(var1, 3)
# now this will add 3 to all the element of the var1 array just like the above,
# with also other subtract, divide we can do this.

print("----------------------------------------------------------------------------")

wholearrminus = np.subtract(var1, var2)  # this will subtract first element from first
# second element from second and so on.
# from its corresponding elements.of the both arrays.
print(wholearrminus)

print("----------------------------------------------------------------------------")

wholearrmultiply = np.multiply(var1, var2)  # this will multiply the corresponding elements.of the both arrays.
print(wholearrmultiply)

print("----------------------------------------------------------------------------")

wholearrdivide = np.divide(var1, var2)  # this will divide the corresponding elements.of the both arrays.
print(wholearrdivide)

print("----------------------------------------------------------------------------")

wholearrmod = np.mod(var1, var2)  # this will find the modulus of the corresponding elements of the both arrays.
print(wholearrmod)
# when we divide some number with other number
# some time it have remainder.
# so basically the modulus function is showing us that remainder value
# if we divide one value with another.
print("----------------------------------------------------------------------------")

# this wil give you the power like this will give you 4 power 2 and will give you the value.
# you can also give one whole array with another whole array like example given below
# var = np.array([1, 3, 4, 5])
# var1 = np.array([1, 3, 4, 5])
#
# whole = np.power(var, var1)
# print(whole)

wholearrpow = np.power(4, 2)
print(wholearrpow)
print("----------------------------------------------------------------------------")

# we can do all these function with 2D...
# 2D

aa = np.array([[1, 2, 3, 4], [1, 3, 4, 5]])
ab = np.array([[1, 2, 3, 4], [1, 3, 4, 5]])
print(aa)
print(ab)

abadd = aa + ab
print(abadd)

# now if done this with the help of function....

abb = np.add(aa, ab)
print(abb)

# just like 1D array it will add corresponding values.
print("----------------------------------------------------------------------------")
# we can also do the subtraction just like addition with function......
# abb = np.subtract(aa, ab)
# abb = np.multiply(aa, ab)

print("----------------------------------------------------------------------------")
# FINDING MAX VALUE
print("max valuessss")
ll = np.array([1, 2, 3, 4])
llmax = np.max(ll)
print(llmax)
print("max value position : ", np.argmax(ll))
print("min value position  : ", np.argmin(ll))


print("----------------------------------------------------------------------------")
# FINDING MIN VALUE.
llmin = np.min(ll)
print(llmin)

# this will also give you the positon of the min value( argmin(array)   )
ll = np.array([4, 16, 88, 36])
llmin = np.min(ll)
llminpos = np.argmin(ll)
print(llmin)
print(llminpos)


print("----------------------------------------------------------------------------")
# FINDING SQUARE ROOT.
llnew = np.array([4, 9, 16, 25, 36])
llsqrt = np.sqrt(llnew)
print(llsqrt)

print("-------------------------------------------")
abcc = np.cos(0)  # this will find you simple the value of cos0 which is 0
print(abcc)

print("-------------------------------------------")
aab = np.sin(0)  # this will find you simple the value of sin0 which is 1
print(aab)

# just like this we can find all the functions of cos,sin etc like this.

print("-------------------------------------------")

# 2D arrays....
"""
so if we want to find the min or max values in 2d array then we also have to give you
the axis value. so the axis 0 shows the column while the axis 1 shows the ros
so if we want to find the min or max value in colum then we have to give axis=0
while if we want to fide min or max value in row then we have t0 pass axis=1

we can also give the argmin or argmax just like for 1d array.

"""
print('finding 2d')
var2d = np.array([[1, 3, 4, 99, 2], [4, 1, 98, 17, 8]])
print(np.min(var2d, axis=0))  # this will show min value in columns.
print(np.min(var2d, axis=1))  # this will show min value in row.
print(np.max(var2d, axis=0))  # this will show min value in column.
print(np.max(var2d, axis=1), np.argmin(var2d))  # this will show min value in row.

