"""
List Iteration...

"""

fruits = ["apple", "mango", "banana", "grapes", 49, 8.2]

# using for loop.
# for i in fruits:
#     print(i)

print("-"*40)

# using for loop with range and length function.
# this will take the range using the length method and by this it will find the range of fruits
# and will iterate that loop that much time.
# for i in range(len(fruits)):
#     print(fruits[i])


# iteration using while loop.
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1



# using shorthand for loop.
[print(i) for i in fruits]  # this is short method for printing value from list using for loop.
# we have to use [] 
