"""
combination of letter etc.

in order to find the type of something we can use type()
methods of string :

length => to find some things length
count => to count something specific
upper => to change to upper case
lower => to change to lower case
index => to find something index
capitalize => will capitalize the first letter of all the string
format =>  in this we can use the string interpolation like thing...
center => by this we can centralize our variable in something

"""

name = "my name is HARRy potter."
print(type(name))
# print(type(age))
print(len(name))
print(name.count('a'))  # now this will count that how  much time 'a' is there
print(name.upper())
print(name.lower())
print(name.index('a'))
print('capitalize')
print(name.capitalize())  # to capitalize only first letter.

#  we can also give some range to find our specific character...

print(name.index("A", 10, 13))
print(name.casefold())
print(name.lower())

print(name.find("R"))


secondName = "Afridi Ullah Khan"
age = 12

bbb = "my name is {} and age is {}"
# print(bbb.format(secondName))  # this will automatically take the secondName variable in the {}

print(bbb.format(secondName, age))  # this will also print age with the name also because we have mention w2 curly brackets

#  we can use center to center something.

thirdName = "john"
print(thirdName.center(10, "*"))  # this will center the name john and also print some *
#  before and after the name.

