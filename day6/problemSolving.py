# Q1 write a program to swap first and fourth element.

a = ["Ross", "Rachel", "Monica", "Joe"]
# a[0], a[3] = a[3], a[0]
# print(a)

# Q2 write a program to add new value to second position
a.insert(1, "NewValue")
print(a)

# Q3 write a program to delete value from 3rd position
print(a)
a.pop(2)
print(a)

# Q4 write a program to multiply all the values of list
b = [12, 4, 25, 23, 8]
multiiply = 1
for i in b:
    multiiply = multiiply * i

print(multiiply)
# multiiply *= i ( same as multiply = multiply * i)

# Q5 write a program to find the largest value from list.

cc = [12, 2, 523, 89, 79, 9, 1, 6, 12]
cc.sort()
print(cc)
print("largest values is : ", cc[-1])
print("smallest value is : ", cc[0])
