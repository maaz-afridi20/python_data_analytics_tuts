"""
String Function part 3:

endswith => return true if the string ends with some given specified value.
startswith => return true if the string starts with some given specified value.
swapcase => swap the lower case to uppercase and upper case to lowercase
strip => this will remove all the whitespace from the string
split => is used to split string and will return it into list.
ljust => if we want to put somthing on the left side of the string
rjust => if we want to put somthing on the right side of the string
replace => in order to replce some value with other...
rindex => 
"""


a = "Harry Potter"
print(a.endswith('R'))

print(a.startswith('H'))

#  we can also mention the range and then check whether the 
#  word is that or not...

#  like
print('-'*30)
print(a.endswith('e', 6, 11))  # now this will take the range from 6 to 11 and
# in this range will check whether the word is ending with this or not.

print('*'*30)
b = "Spider Man"
print(b.startswith('S'))
# we can also give them a range just like the endswith
# and in that range it will start to check the startswith and will return true or false.


c = "SWap caSE"
print(c.swapcase())

d = "      empty spacess     "
print(d.strip())

# we can also mention that we want to remove * or . just like that by mentionning it.

e = "     *** empty space ... "
print(e.strip("*, ., "))  # now this will remove all the spaces as well and also the * and .

print("-"*40)
f = "abc#def#fha#sf"
print(f.split("#"))

g = "my name is ali. i am boy. i am in pakistan"
print(g.split("."))  # this will split this string on . and will write it in list.

print("-"*40)
h = "harry potter"
i = h.ljust(20, "*")
print(h, "is my fav movie")

#  this is just like the ljust it will give some spaces or we can also specify
#  some * or anything to the right side.

print("-"*40)
hh = "harry potter"
ii = hh.rjust(20, "*")
print(ii, "is my fave")


print("-"*40)
nameeee = "my name is kkhan"
print(nameeee.replace("kkhan","john"))  # first value is that value which we want to replce and
#   second value is that value by which we want to replace that value

