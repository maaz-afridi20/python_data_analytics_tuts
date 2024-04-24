"""
Math Module : it contains diff type of functions like min, max, power etc
"""
import math
a = max(89, 29, 18, 99, 9)
print("max value is", a)

b = min(9, 13, 99, 100, 48, 3)
print("min value is", b)

c = pow(4, 2)  # so basically this mean 4 ka square
d = pow(2, 5)  # this mean 2 to the power 5
# we can also use them math.pow(2,4) and so on.
print(c)
print(d)

squareRoot = math.sqrt(36)  # this will just give simple square root of 36
print(squareRoot)


cd = abs(-23)  # this will just give you the abs value like
# it will give the value in positive. if we give it any value in minus it will return the
# same value in positive.
cddd = abs(-100)
print(cddd)
print(cd)


k = math.ceil(1.3)  # iss ka main function point walay values mein use hota hai k
# jab humein koii b value point mein return ho rahi hoti hai tu ye uss ko
# round off kr dega magar ye round off next big number ki taraf karega. like
# agar 2.1 hai tu ye humein 3 print karega... agar ye 2.8 hai phir b 3 print kr k dega. and so on.
kk = math.ceil(4.5)
print(kk)
print(k)

zy = math.floor(2.8)  # so the main diff between the floor and ceil is that k ceil humein agay wali
# value to return karega point mein orr ye
# floor humein previous low wali value ko return karega chahay jo b value ho...
zyy = math.floor(8.9)  # it will print 8
print(zy)
print(zyy)
