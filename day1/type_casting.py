"""
Type casting... 👇

there are 2 type of type casting.

1 implicit 👇
    where the python does conversion by itself.
2 explicit 👇
    where the user does the conversion by them. from one datatype to another.


=> for knowing what type of the type cast is this we can use (type) keyword.

if we want to convert the string a to the int a than we can use like int(a)
this will simply change the string a to int a

so jiss mein b hm change krna chahtay hain siraf uss variable ko
hmm uss type cast mein likhengay... like k
agar humein string variable ko int mein change krna hain tu humein
uss ko like a='323' => int(a)
tu ye a ko int mein change kr dega.

we do the same things with the other data types like float,string bool etc.

"""

name = "john.."
print(type(name))

age = 23
print(type(age))


a = "42"
print(int(a))  # this will change the string a to the int a
# print(type(int(a)))

# Method 1 of swapping values
# Swapping the values of two variables...

x = 10
y = 20
print(f"original value of x :{x} and y:{y}")
temp = x
print(f"temp value is {temp}")
x = y
print(f"now x value is {x}")
y = temp
print(f"now y value is {y}")

print("the value off X is ", x)

# Method 2 of swapping values
# now this method will automatically swap the values of a into b
aa = 20
bb = 30
aa, bb = bb, aa
print(aa)
print(bb)
