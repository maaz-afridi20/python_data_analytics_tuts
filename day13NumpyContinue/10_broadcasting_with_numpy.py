"""
BroadCasting With Numpy:

jab hm addition krtay hain arrays ki tu uss k dimension agar same na hon tu ye
addition nai karega... orr broadcasting error dega.
broadcasting orr kuch b nai siraf ye batata hai k addition etc mein koii error
anay ki waja kiaa hai etc like k addition etc k liye kia zaroori haiii
baki details given below.....

1)  tu sab say pahlay broadcasting ka rule ye hain k same dimensions honay chahiyee.
2)  agar same dimension na hon tu agar rows of first and column of second same hu
    tab addition hoga warna nai hoga.
    just like simple matrix addition or subtraction or multiplication
    k if the dimensions are not same then the rows of first matrix and column of second matrix
    should be same.
    just the basic matrix chapter
    if the dimension is not same of the two arrays then we have to
    check some of these points.
    which is if the dimensions are not same then
    (rows of first and columns of second should be same) otherwise not possible

    simple si logic ye hain k ya tu dimension same hongay chahiyee jaisay b ho..
    phirr addition ho jaye gi
    ya phir agar same nai hain dimensions tu phir
    rows of first and columns should be same.

"""
import numpy as np

var1 = np.array([1])
var2 = np.array([[1], [2], [3]])
print(var1 + var2)


