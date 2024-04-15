"""
{
👉 1 Arithmetic operators {+,-,*,/,**,//,%} 👇
in order to write something in power we have to use ** like  10**2 this mean that 10
raise to power 2
% this operator is called modulus and this helps to find remainder
// => this is called float division this mean that if we use this, this will
not give the values in the points. this will give all the values of quotient etc but not
the point values. point k baad ki value ko count nai karega
}

{
👉 2 Comparison operators {==,=>,<=,>,<,!=} 👇
to compare things
}

{
👉 3 Logical operators{and, or, not}
agar hm and use karein orr iss mein agar dono values true hon
phir true return hoga.
agar hm or use karein orr uss mein aik value b true ho tu true return hoga.
agar hm kisi k cheez sath b not use karein tu wo uss cheez ko
reverse kr dega. like agar hm true k sath not lagayein tu ye false ho jaye. ga
}

{
👉 4 Assignment operators (=,+=,-=,*=)
to assign values to something
}
{
👉 5 Identity operators (is, isNot)
iss mein hm check krtay hain k ye cheez ye wali hai ya nai.
like agar hm x is str tu ye true or false return karega k ye x jo hai string hai ya nai
}
{
👉 6 Bitwise operators (AND(&), OR(|), XOR)
this bitwise operators is used to compare the binary operators
so now in order to find the bit number of some value we have to use bin(10)
this will print the binary value of 10
& will return us   0,0 = 0
                   1,0 = 0
                   0,1 = 0
                   1,1 = 1
or will return us  0,0 = 0
                   1,0 = 1
                   0,1 = 1
                   1,1 = 1
Xor => this say that when there is similar item will give us 0 while dis similar value will give us 1
                   0,0 = 0
                   1,0 = 1
                   0,1 = 1
                   1,1 = 0
this bitwise operators is only use on the binray values
}
{
👉 7 Membership operators(in, notIn)
these operators are use when we want to check that if these are the members of
the another variables or not
print("p" in name) this will check that is there p present in the name variable
than will return true or false
print("v" not in name) this says that k v is not in the variable name
and this is true because v is not present in name variable.
}

"""

print('operators and operands...')

a = 10
b = 10
c = 8
d = 3

print("addition... ", a+b)
print("subtraction... ", a-b)
print("multiplication...", a*b)
print("division...", a/b)
print("power values...", a**2)
print("modulus...", a % b)
print("floor division.", c//d)

# power = int(input('enter number... : '))
# check = power**2
# print(check)

print("---------------------------------")
print("Comparison Operators.")
print(3 > 2)
print(3 < 2)
print(3 == 2)
print(3 != 3)
print(3 >= 2)

print("---------------------------------")
print("Logical Operators")
print(3 > 2 and 11 > 10)  # this will return true. because both condi are true
print(3 > 2 or 3 > 19)
print(not (3 > 2 and 10 > 5))  # this will return false due to not.

x = 10
print("x is ", x)
x += 6
print("x after plus.. ", x)
x -= 6
print("x after minus.. ", x)
x *= 10
print("x after multiplication.. ", x)

print("---------------------------------")
print("Identity Operators")
age = 10
bage = "10"
print(age is bage)  # this will return true or false.
# that the above age is same as the bage or not.
# this will return false because the age is int while the bage is string.

print(age is not bage)  # this will return true because age is not same as bage.

print("---------------------------------")
print("bitwise Operators")
print(bin(10))  # this will print the binary value of 10
print(bin(100))
print(8 & 2)  # this is and operator for bitwise operations.
print(10 | 8)

print(10 ^ 8)

print("---------------------------------")
print("membership Operators")
name = "ali"
print("p" in name)
print("v" not in name)
