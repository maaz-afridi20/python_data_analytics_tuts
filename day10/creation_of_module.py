"""
Creation Of Module :
if we want to create our own module we can do that
we just have to create a file with .py extension
no in that file any type of code we can write and use them
just like in built modules we have to import that module where we want to use it.

the demo module is our own-created module and we have imported it.
now in that demo module any type thing we can use it here like
in demo module there is addition function so by importing the demo module
we can use that addition function here in this file.

we can also use alias for any module like
import math as mmm    etc.
import datetime as mydatetime  etc...



we can create any thing in our own module.

"""
import datetime
import demo as mydemo

now = datetime.datetime.now()
print(now)


value = mydemo.addition(10, 28)
print("value of addition : ", value)

checking_name = mydemo.checking_dict["name"]
print(checking_name)

checkingg = mydemo.checking_dict  # will print whole dict in that demo module.
print(checkingg)

