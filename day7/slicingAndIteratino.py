"""
slicing and iteration.
"""

a = ("onplus", "vivo", "iphone", "samsung", "huawei")
print(type(a))
print(a[1:3])
print(a[:3])    # will print 3 values.
print(a[::3])   # will print all the values having gap of 2
print(a[::-1])  # will print the whole tuple in reverse.


for i in a:
    print(i)

# along with range and length in the for loop.
for i in range(len(a)):
    print(a[i])


# with while loop.
print("-"*60)

n = 0
while n < len(a):
    print(a[n])
    n += 1
