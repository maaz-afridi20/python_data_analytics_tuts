"""
List Comprehension :

"""

l1 = [30, 40, 50, 60, 70]
l2 = []

for i in l1:
    if i > 40:
        l2.append(i)


print(l2)

"""
like above, we can see that in order to add something in the new list l2 we used 
for loop. this method can also be used but by list comprehension we can do it quickly. 
like below
"""

l3 = [i for i in l1]  # just by this line all the element of l1 will be added to l3
print("l3", l3)

"""
we can also use some conditions or filter the statements. like the above one.
but this list comprehension method will only be used when we want to copy all the 
data of one list to another.
"""

print('---')
l4 = [i for i in l1 if i > 40]
print("l4 ", l4)
