"""
Modules : modules are functions in which code are already written
we have to import them, and we can use them.
modules may be in built

we can also create a module and then can use them.


In-BuiltModules :

Datetime: it's used to work with all the functions related to date.
Random:
Math:
"""

import datetime

x = datetime.datetime.now()
print(x)

y = datetime.datetime(1999, 6, 15)
print(y)

# in order to know the day at that date we can use the strftime

print(y.strftime("%A"))  # this will the day with whole spelling on that date.
print(y.strftime("%a"))  # this will the day with small spelling on that date.
print(y.strftime("%B"))  # this will print the month name
print(y.strftime("%m"))  # this will print month in number like 6, 10 , 12  month etc.
print(y.strftime("%Y"))  # will print whole year like  1999
print(y.strftime("%y"))  # this will print small year like 99 or 23, 24 etc

