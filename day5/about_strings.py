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

isalnum => return true if all character in string are alphanumeric(mean it contain alphabet and numbers both)
isdecimal => return true if all character in string are decimal
isalpha => return true if all character in string are alphabet
isdigit => return true if all character in string are digit(if there is . then also it will return false
isnumeric => return true if all character in string are numeric
islower => return true if all character in string are lower case
isupper => return true if all character in string are upper case
isspace => return true if all character in string are white spaces
istitle => return true if the string follow the rules of title
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

print("-"*30)
newName = "this is new name"
hello = "helloworld1233"
cc = "42323"
d = "13.34"
print(newName, newName.isalnum())
print(newName, newName.isdecimal())
print(newName, newName.isalpha())
print(newName, newName.islower())
print(newName, newName.isupper())
print(newName, newName.isspace())
print(hello, hello.isalnum())
print(cc, cc.isalnum())
print(d, d.isdigit())


print(cc, cc.isdecimal())
print(cc, cc.isnumeric())  # will return true if the characters are digits


blank = "   "
print(blank.isspace())  # it only checks the blank spaces
# if it only contains all white spaces then it will return true

chekss = "Checking This String"
print(chekss.istitle())  # this will return true because the first string of all letter is capital

