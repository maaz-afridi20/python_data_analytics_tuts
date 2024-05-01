"""
Starting Date : 26-04-2024
Numpy :
What is numpy?:
it is a fundamental package for doing scientific computation in python.
it provides you multidimensional array.
it's very fast.


Array:
array is just like a list. it contains multiple values.
array may be one dimensional(1D), or may be two-dimensional(2D) and also 3D Array and also multidimensional array.

Array is defined as => a collection of items that are stored in a contiguous memory location.
a contiguous memory location mean that when we take a simple list for example
k agar list mein 3 element hain tu wo memory mein jo b location hongay tu wo waha store ho jayengay
like k agar wo teeno element nazdeek nazdeek agar na b hon, k aik ko kahi jagah mill gayee
dosray ko kahi jagah, magar wo store ho jayengay....

on the otherside jo array hai wo aisay nai hai.. agar array mein 3 elements hongay tu
wo teeno agary aik sath nazdeek hii jagah milay store hongay kii tu wo store hongay warna nai hongay store
matlab k array beech mein kahin b space naii chahta element k beech mein..

array consumes less memory.
fast as compared to list.

when we print the list the values are comma separated, while in array there is no comma

to install numpy use [pip install numpy.]

if we want to use wide variety of mathematical operation we use numpy.
it has very libraries.

it also helps very much in doing machine learning thing, data science.
logical, shapes manipulation, sorting, selecting etc all these functions can be done easily
with the help of numpy.

"""


import numpy as np

x = np.array([1, 2, 3, 4])
print(x)
print(type(x))
