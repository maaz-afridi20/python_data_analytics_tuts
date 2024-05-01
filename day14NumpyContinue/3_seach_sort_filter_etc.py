"""
SEARCH, SORT, FILTER FUNCTIONS ETC.



SEARCH :
for searching some value in array, also finding the index value of that
that type of functions can be done through search method.
for this we have to use "WHERE" keyword.


SEARCHSORTED KEYWORD:
for using search sorted array the array must be sorted.
agar hm chahtay hain k koii kisi value ko array k andar put karein tu
ye jo search keyword hai tu sab say pahlay humein bataye ga k aap
konsi jagah pr is ko put kr sktay hain
for eg
agar humaray pass 1 say lekar 100 tk values hain array mein tu agar humein put krna hai 40 ko
tu jab humein
aa = np.array([10, 20, 30, 35, 60,80])
x = np.searchsorted(aa,25 )
iss tarah ko put krna hai tu ye humein batay gaa k konsii index k baad aap value put kr sktay hain
values agar sort hon array mein.. tab
even we can place a whole list inside this. like
x = np.searchsorted(aa,[25, 28, 29] )


SORT :
if we want to sort array we can use this funciton...
it may b of string, or any integers etc. we can use .sort() method.


FILTER :
filter humein koii b specific value ko filter kr k deta hai array sy
just like view and copy jab b hm filter ka function use krty hain
tu ye jo new filtered values hain uss ko new array mein save kr lega..
jo b new array hogii uss mein siraf new filtered values hi hongiii....
tu jo value humein chahiyee humein wahan true passs krna haii or jo naii chahiyee
waha false pass krna hai..
aa = np.array(['bb','asdf','fa','sad','aa'])
ff = [True, False, True, False, True]
newvar = aa[ff]
print(newvar)

so just like this. ooper hm nay list mein values ko true,false likhaa hai
tu jo b value uss index prr hogii tu jaha true hoga wo new
filtered aray mein mill jaye gii orr jaha false hoga wo nai milegi
iss tarah values filtered ho jayengi...

"""
import numpy as np

# ----------------------------------------------------------------------------------------------------------
# WHERE KEYWORD
aa = np.array([22, 44, 22, 89, 22, 80, 89, 73, 22, 90, 58, 10, 43, 22])
x = np.where(aa == 22)
print(x)

"""
now the above function will give you the index of 22 that where 22 is repeated or present
also it will give you the datatype of that value.
we can perform many other functions like
x = np.where( aa/2 == 10)
so this will give you that value when divided by 2 and gives a value 10
also other functions like modulus, multiply can be perform.....
x = np.where( aa % 2 == 0)
"""
# ----------------------------------------------------------------------------------------------------------
# SEARCHSORTED KEYWORD
bb = np.array([10, 20, 30, 35, 60, 80])
bbx = np.searchsorted(bb, 25)
print(bbx)

# ----------------------------------------------------------------------------------------------------------
# SORT KEYWORD....

aa = np.array([30, 20, 10, 44, 400,40])
x = np.sort(aa)
print(x)

# for sorting strings..
aab = np.array(['bb','asdf','fa','sad','aa', 'awe','mzd'])
print(np.sort(aab))

# it can also sort 2D arrays...
# aa = np.array([[3,1,6],[9,10,2],[22, 32, 8]])
# print(aa.ndim)
# print(np.sort(aa))

# ----------------------------------------------------------------------------------------------------------
# FILTER KEYWORD :

aa = np.array(['bb','asdf','fa','sad','aa'])
ff = [True, False, True, False, True]
newvar = aa[ff]
print(newvar)

# we can also use this...
a = np.array([10, 4, 5, 8, 19, 48, 88])
bb = a > 10
cc = a % 2 == 0
print(a[bb])
print(a[cc])
# this will only print, or we can say that filter that values which are greater than 10
# just like this we can use any condition and filter that values.

