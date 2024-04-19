"""
String Slicing :

"""

movie = "harry potter and goblet of fire"
print(movie)
print(movie[0])
print(movie[0:5])
print(movie[6:12])  # this will print only potter...

print(movie[:5])  # this will take the first value 0 by default

# we can also use negative values like

print(movie[-4:])   # so this will print the values from "fire"
# if we use - then we have to count from negative side...

# if we do not write the ending value then it will go to the end by default

print("-"*40)
b = "07490278940858208720329924"
print(b[:: 2])  # now this will do slicing from start to end, but it will have a gap of 2
print(b[:7:2])  # now this will do slicing from start to 7 having gap of 2.

# we can give a gap of as much number we want.

print(b[::4])

#  if we want to just print the reverse in slicing then we can use -1

print(b[::-1])  # this will print slicing from end to start having the gap of 1
print(b[13:0:-1])   # will print from 8 but in the negative direction up to starting point
print(b[8])

