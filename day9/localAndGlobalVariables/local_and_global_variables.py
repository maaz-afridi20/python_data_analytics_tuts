"""
Local Variables :
local variables are only restricted to only one block of code.
and cannot be changed throughout the program.

for example if we declare any variable x = 10,
and we have one function, and we want to change the value of x in that variable
tu ye uss ki jo function say bahir ki value hai x ki wo change naii hogii.. wohi ki wohi rahegi.
example given below...


Global Variables :
they are not restricted in one block of code.
it can be accessed at anywhere in program.
magar agar hm yehi same concept global variable prr use karein tu
for eg agar aik global variable hai orr uss ki value hm agar koii specific any point prr
change kr lein koi function mein b change kr lein tu uss ki value sari jagah pr change ho jaye gi

so tu agar humein koii global variable ko use krna haii tu humein
(global) keyword ka use krna hoga tab ye global variable hogaa orr kahin b
ye keyword k sayh hm koi variable declare karein orr value uss ki change karein tu
ye sary k saray program mein uss ki value change ho jaye gi...
"""

x = 20


print("value before function ", x)

def hell():
    x = 30
    return x


print(hell())


print("value before after ", x)

# now still the value of x will bo 20 it will only be changed inside that function
# but not the outside of the function.

def hell2():
    global x
    x = 40
    return x


print(hell2())

print("value before after ", x)