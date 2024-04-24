"""
Module Random :
it helps us to pick some value random.

"""

import random

x = random.randint(1, 10)  # this will pick any random int in between 1-10
print(x)

listy = ["fuck", "you", "and", "this", "world"]

y = random.choice(listy)  # now this will pick any random string from this list. # we will use choice()
print(y)

