# write a program to sort the dict by value.
# we can use sorted() function.

a = {"a": 12, "b": 23, "c": 0, "d": 89, "e": 30}
a = sorted(a.values())


# write a program where the keys of dict will be numbers from 1 to 15 and their
# values will be their squares.
newDict = {}
for x in range(1, 16):
    newDict[x] = x**2

print(newDict)


# write a program to multiply all items in dictionary
product = 1
addition = 0
d = {"a": 1, "b": 2, "c": 8, "d": 3, "e": 2}
for i in d:
    product *= d[i]  # this will print the product of all the values of the dict.
print(product)

for i in d:
    addition += d[i]  # this will print addition of all the values of dict.
print(addition)
"""
ye *=  iss ka matlab hai k ye value ko le ga b orr sath sath multiply 
kr k next bo hota jaye gaa same isse tarah hm plus k sath b kr sktay hain like
+=  iss ka matlab haii k ye value ko add b krta jaye ga orr next b hota jaye. ga.
"""


# write a program to sort dict using keys.

bc = {12: "a", 23: "b", 0: "c", 89: "d", 30: "e"}
print(sorted(bc.keys()))
