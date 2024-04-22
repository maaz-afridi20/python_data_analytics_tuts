"""
PROBLEM SOLVING

"""

# write a program to find min and max in set.

a = {12, 42, 25, 1, 88, 100, 8}
b = {12, 44, 89, 17, 981, 41, 100, 42, 88}
maximum = max(a)
minimum = min(a)

print("max value is ", maximum)
print("min value is ", minimum)


print("---------------------intersection--------------------------")
# write a program to find common elements in set.
intersection = a.intersection(b)
print(intersection)

print("---------------------difference--------------------------")
difference = a.difference(b)
print(difference)


print("---------------------finding common--------------------------")
# write a to find common elements in 3 list using sets.

d = [1, 2, 4, 5, 8]
e = [9, 6, 5, 19, 20]
f = [5, 11, 100, 89, 10]

# first we have to convert these lists to sets.
# then it will automatically only print that element that are
# present in all the sets. because we are using &

print(set(d) & set(e) & set(f))


print("---------------------remove something from set--------------------------")
# delete something from set.

# if we use remove method for deleting something then the element must have to be present in the set
# if that element is not present in the set then it will throw error
g = {"ali", "khan", "ullah", "afridi", "next"}
g.remove("ullah")
g.discard("aliii")  # this element is not present in set still it will not throw any error
                    # nothing will happen.
print(g)

# there is another method .discard()
# so if we use this this will also delete something from set
# if we put name of something for deleting if that element is not present it will not throw
# any error
# if that element is present it will delete that element but if not present that element
# it will not throw any error.

print("---------------------checking subset of another set --------------------------")

print(a.issubset(b))
