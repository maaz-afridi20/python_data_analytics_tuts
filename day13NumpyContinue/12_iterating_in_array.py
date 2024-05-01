"""
ITERATING IN ARRAY :
for looping in something.

so if we want just simple method this is done through for loop
if we have 1D array we use 1 for loop, if we have 2D array we use 2 for loops,
if we have 3D array we use 3 for loops.

so if we didn't want to use all these loops then we also have method
by using that method it can be very easily done.

method name => .nditer()

if we want to get the value and also want to get
the index value in which that value is store in array
then we can use ==>>  np.ndenumerate()
this will print the value of array and also
will print index value of that value.

"""

import numpy as np

# kk = np.array([1, 8, 8, 18, 4, 18, 100, 48, 32, 24, 98, 135, 4, 88, 82])
# for i in kk:
#     print(i)


# print("length : ", len(i))


# for 2D array we have to use for loop two time

ll = np.array([[100, 48, 32, 24, 98, 135], [1, 8, 8, 18, 4, 18]])
for i in ll:
    for j in i:
        print(j)

# so through for loop this will goto the first index and will
# print all the elements through the second for loop. and then
# this will goto the 1 index and will print all the element
# of the 1st index because of the second loop.

# now if using for 3D array we have to use 3 for loops. just like
aa = np.array([[[100, 48, 32, 24, 98, 135], [1, 8, 8, 18, 4, 18],[31, 32, 19, 22, 1, 65]]])

for i in aa:
    for j in i:
        for k in j:
            print(k)
# this will print all the values one by one.
# so jitnay dimensions ka array hoga utnay hi times humein loops laganay hain
# for iteration and getting values.
#
# ------------------------------------------------------------------------------------------------

"""
agarr hum bar bar for loop use nai krna chahtay tu hum nditer functino ko use kr 
k sari values get kr sktay hain... chahay kitnay dimensions ki array b hon 
siraf aik baar nditer() ko for loop mein use karein orr sari values get ho jayengi..
example given below...
"""

print("-----------------------------------------------------------")
# using nditer for 1D
kali = np.array([1, 8, 8, 18, 4, 18, 100, 48, 32, 24, 98, 135, 4, 88, 82])
for i in np.nditer(kali):
    print(i)
print("-----------------------------------------------------------")
# using nditer for 2D
ll = np.array([[100, 48, 32, 24, 98, 135], [1, 8, 8, 18, 4, 18]])
for kk in np.nditer(ll):
    print(ll)
print("-----------------------------------------------------------")
# using nditer for 3D
aa = np.array([[[100, 48, 32, 24, 98, 135], [1, 8, 8, 18, 4, 18],[31, 32, 19, 22, 1, 65]]])
for cc in np.nditer(aa):
    print(cc)

# this will work same like using all these loops for iterating...
"""
agar hm chahtay hain k ye values iterate hon magar uss k sath
sath uss ki indexing b show hon tu hm.. nditer() ki jagah hm 
ndenumerte()  => iss ko use kr sktay hain.. 
tu iss mein ye karega k value tu dega magar uss ki indexes b dega. 
k ye value konsay index pr hain..
example below.
"""
aa = np.array([[[100, 48, 32, 24, 98, 135], [1, 8, 8, 18, 4, 18],[31, 32, 19, 22, 1, 65]]])
for i in np.ndenumerate(aa):
    print(i)
